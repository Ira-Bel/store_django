from django.shortcuts import render
from .models import Products, Orders
from django.http import HttpResponseRedirect, Http404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404


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


@method_decorator(login_required, name="dispatch")
class CreateOrder(View):
    template = "create.html"
    model = Orders

    def get(self, request):
        return render(request, self.template)

    def post(self, request, order_sum=None):     #   ИЗМЕНИТЬ!!!
        order = request.POST.get("id_product", "")
        count = request.POST.get("count", "")
        if order and count:
            self.create(count=count, order_sum=(count*request.products.cost), user=request.user, product=request.products)
            return redirect("home")

        return render(
            request,
            self.template,
            {
                "count": count,
                "order_sum": order_sum,
            }
        )

    def create(self, **kwargs):
        print(kwargs)
        order = self.model(**kwargs)
        order.save()

