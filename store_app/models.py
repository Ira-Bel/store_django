from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Product(models.Model):
    name = models.CharField(max_length=60)
    count = models.IntegerField(verbose_name="кол-во")
    cost = models.IntegerField(verbose_name="стоимость")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    order_count = models.IntegerField(20)
    order_sum = models.IntegerField(20)
    order_datetime = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Ticket(models.Model):
    uuid = models.UUIDField(max_length=32)
    available = models.BooleanField(default=True, null=True)
    user_id = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True, blank=True)

    @staticmethod
    def valid_ticket(input_uuid) -> bool:
        if len(str(input_uuid)) == 36:
            try:
                ticket = Ticket.objects.get(Ticket.uuid == input_uuid)
                if ticket.available:
                    return True
            except Ticket.DoesNotExist:
                return False
            else:
                return True
        else:
            return False


def py():
    return None
