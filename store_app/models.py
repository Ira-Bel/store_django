from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Products(models.Model):
    name = models.CharField(max_length=60)
    count = models.IntegerField(20)
    cost = models.IntegerField(20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Orders(models.Model):
    count = models.IntegerField(20)
    order_sum = models.IntegerField(20)
    order_datetime = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)

