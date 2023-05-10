from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    seriaizer = ProductSerializer(data=request.data)
    if seriaizer.is_valid(raise_exception=True):
        instance = seriaizer.save()
        print(instance)
        return Response(seriaizer.data)
    
    return Response({"invalid": 'not good data'}, status=400)
