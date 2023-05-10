from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list
    get -> retrieve
    post -> create
    put -> update
    patch -> Partial update
    delete -> destroy
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    
class ProductGenericViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin, 
                            viewsets.GenericViewSet):
    '''
    get -> list
    get -> retrieve
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

product_list_view = ProductGenericViewSet.as_view({'get':'list'})
produt_retrieve_view = ProductGenericViewSet.as_view({'get':'retrieve'})
 
    