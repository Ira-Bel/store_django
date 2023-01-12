from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=60)
    count = models.IntegerField(20)
    cost = models.IntegerField(20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


