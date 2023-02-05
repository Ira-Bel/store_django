from django.contrib import admin
from . import models


# Register your models here.
# admin.site.register(Product)

admin.site.register(
    [
        models.Product,
        models.Order,
        models.Ticket,

    ],
)
