from decimal import Decimal
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id','title','price','featured','category','category_id']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id','username','first_name','last_name','email','password']
        fields = '__all__'
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
