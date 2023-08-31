from rest_framework import serializers

from .models import (
    Category,
    Booking,
    Menu
);

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        exclude = ['user']
    


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

  

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        exclude = ['user']