from rest_framework import serializers

from .models import (
    Cart,
    Category,
    Order
);

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ['user']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['user']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['user']