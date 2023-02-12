from rest_framework import serializers
from ...models import Product, Order, Ticket

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source="product", read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["cost"]


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ["available", "user_id"]
