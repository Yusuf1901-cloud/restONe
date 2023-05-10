from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(
                            UserQuerySetMixin,
                            StaffEditorPermissionMixin,
                            generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)
        # send a django signal
     
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs) 
    #     user = self.request.user
    #     # print(user)
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=user)
        
class ProductDetailView(
                        UserQuerySetMixin,
                        StaffEditorPermissionMixin,
                        generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
        
           
class ProductUpdateView(
                        UserQuerySetMixin,
                        StaffEditorPermissionMixin,
                        generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    # def perform_update(self, serializer):
    #     if not serializer.content:
    #         serializer.content = "Perform updatedagi content"
    #     return super().perform_update(serializer)
    
    
class ProductDeleteView(
            UserQuerySetMixin,
            StaffEditorPermissionMixin,
            generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
      
    def perform_destroy(self, instance):
        # instance 
        return super().perform_destroy(instance)
    
    
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method 
    
    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product, id=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        query = Product.objects.all()
        data = ProductSerializer(query, many=True).data
        return Response(data)
    
    if method == 'POST':
        # create
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": 'not good data'}, status=400)

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin,
    generics.GenericAPIView
    ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content', None)
        
        if not content:
            content = title
        serializer.save(content=content)
        
        return super().perform_create(serializer)
    
    def update(self, request, *args, **kwargs):
        print(request)
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        
        return super().destroy(request, *args, **kwargs)