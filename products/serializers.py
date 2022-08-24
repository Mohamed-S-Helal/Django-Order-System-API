from rest_framework import serializers
from .models import Product, Purchase
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    created_products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'created_products')
        

class PurchaseSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.id')
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Purchase
        fields = ('id', 'product', 'user')

        
        
# class PurchaseProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['purchasers']
        
        ## I am stuck here


