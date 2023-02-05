from django import template
from store_app.models import *

register = template.Library()


@register.simple_tag()
def get_product():
    return Product.objects.all()
