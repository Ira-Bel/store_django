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
        id_user = request.user
        prod_id = request.POST.get("prod_id")
        product = Product.objects.get(id=prod_id)
        order_count = request.POST.get("amount")
        id_ticket = request.POST.get("id_ticket")
        ticket = Ticket.objects.get(id=id_ticket)
        a = Product.objects.get(id=prod_id).cost
        b = Product.objects.get(id=prod_id).count
        if int(order_count) <= int(Product.objects.get(id=prod_id).count):
            points = 0
            if product and order_count and ticket:
                points += 20
                order_points = (int(order_count) * int(a))
                if points >= order_points and int(b) >= int(order_count):
                    order = Order(
                        product=product,
                        user=request.user,
                        order_count=order_count,
                        order_sum=order_points,
                        )
                    order.save()
                    ticket.user_id = id_user
                    ticket.available = False
                    ticket.save(update_fields=["user_id", "available"])
                    product.count = int(b) - int(order_count)
                    product.save(update_fields=["count"])
                    points -= int(order_points)
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

