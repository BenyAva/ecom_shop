from rest_framework import serializers
from .models import Product, Review, Order, OrderItem, ShippingAddress
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    product = ProductSerializer(many=False)

    class Meta:
        model = Review
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    order_items = OrderItemSerializer(many=True)
    shipping_address = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_shipping_address(self, obj):
        try:
            shipping_address = ShippingAddress.objects.get(order=obj)
            serializer = ShippingAddressSerializer(shipping_address)
            return serializer.data
        except ShippingAddress.DoesNotExist:
            return None


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
