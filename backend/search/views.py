from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

from . import client

class SearchListVIew(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        
        user = None
        if request.user.is_authenticated:
            user = request.user.username
            
        query = request.GET.get('q')
        public = request.GET.get('public') != '0'
        taga = self.request.GET.get('tag') or None
        # print(query, public, taga, user)
        results = Product.objects.none()
        if not query:
            Response('', status=404)
        results = client.perform_search(query, tags=taga, user=user, public=public)

        return Response(results)


class SearchOldListVIew(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        print(q)
        results = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)       
        return results