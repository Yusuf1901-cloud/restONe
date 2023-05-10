from rest_framework.reverse import reverse
from rest_framework import serializers

from api.serializers import UserPublicSerializer
from .models import Product
from . import validators

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    # related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    title = serializers.CharField(validators=[validators.validate_title_no_hello,
                                             validators.unique_product_title])
    body = serializers.CharField(source='content')
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk', 
            'title',
            'body',
            'price',
            'sale_price',
            'discount',
            'path',
            'endpoint',
        ]
    
    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }
         
    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user,  title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'this {value } exists already')
        # bu serializerni ichida faqat tushunish uchun qo'yilgan ejan ukam xopmi?
    #     return value
    
    
    def create(self, validated_data):
        # email  = validated_data.pop('email')

        obj = super().create(validated_data)
        # print(obj, email)
        return obj

    # def update(self, instance, validated_data ):
    #     content = validated_data.get('content', None)
    #     if content is None:
    #         instance.content = 'Hi, there you will miss what is going on!!!'
    #     email = validated_data.pop('email')
        
    #     return super().update(instance, validated_data)
    
    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        
        if not isinstance(obj, Product):
            return None
        
        return obj.get_discount()

    def get_edit_url(self, obj):
        request = self.context.get('request', None) # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs = {'pk': obj.pk}, request=request)
    