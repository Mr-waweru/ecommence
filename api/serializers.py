from rest_framework import serializers
from django.contrib.auth import get_user_model
from products.models import Product, Category
from orders.models import Order

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ("id", "username", "email")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    # def validate(self, value):
    #     # Check for case-insensitive uniqueness
    #     if Category.objects.filter(name__iexact=value).exists():
    #         raise serializers.ValidationError("A category with this name already exists.")
    #     return value
    # After the code above(#)handle the error using a try-except block in views.py.


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"