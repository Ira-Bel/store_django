from django.shortcuts import render
from .models import Products
from django.http import HttpResponseRedirect, Http404
from django.views import View


def base_page(request):
    return render(request, "main.html")


def second_page(request):
    return render(request, "page2.html")


def sign_in(request):
    pass


# def show_products(request):
#     list_prod = Products.objects.all()
#     return render(request, "table.html", {"list-prod": list_prod})

class ShowAllProducts(View):

    def get(self, request):
        list_prod = Products.objects.all()
        return render(request, "table.html", {"list_prod": list_prod})
