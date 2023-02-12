from rest_framework import viewsets, pagination

from .serializers import ProductSerializer, OrderSerializer, TicketSerializer
from ...models import Product, Order, Ticket


class ProductPaginator(pagination.PageNumberPagination):
    page_size = 10


class ProductControlViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_id"
    pagination_class = ProductPaginator

class OrderControlViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = "order_id"


class TicketPaginator(pagination.PageNumberPagination):
    page_size = 10


class TicketControlViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_url_kwarg = "ticket_id"
    pagination_class = TicketPaginator
