from .models import Product, Order, Ticket
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


class ShowAllProducts(View):

    def get(self, request):
        list_prod = Product.objects.all()
        return render(request, "table.html", {"list_prod": list_prod})


@method_decorator(login_required, name="dispatch")
class CreateOrder(View):

    def get(self, request):
        return render(request, "create.html")

    def post(self, request):
        prod_id = request.POST.get("prod_id")
        product = Product.objects.get(id=prod_id)
        order_count = request.POST.get("amount")
        ticket = request.POST.get("ticket")
        a = Product.objects.get(id=prod_id).cost
        if int(order_count) <= int(Product.objects.get(id=prod_id).count):
            points = 0
            if product and order_count and ticket:
                points += 20
                order_points = (int(order_count) * int(a))
                if points >= order_points:
                    order = Order(
                        product=product,
                        user=request.user,
                        order_count=order_count,
                        order_sum=order_points,
                        )
                    order.save()
                    return redirect("profile")
        return render(request, "create.html", {"order_count": order_count})


class ShowOrder(View):

    def get(self, request):
        created_order = Order.objects.all()
        return render(request, "order.html", {"created_order": created_order})


@method_decorator(login_required, name="dispatch")
class Profile(View):

    def get(self, request):
        user = request.user
        user_order = Order.objects.filter(user=user)
        return render(request, "profile.html", {"user_order": user_order})


class ShowTickets(View):

    def get(self, request):
        tickets_all = Ticket.objects.all()
        return render(request, "tickets.html", {"tickets_all": tickets_all})

