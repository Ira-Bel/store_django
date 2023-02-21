from .models import Product, Order, Ticket
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404


def base_page(request):
    return render(request, "main.html")


def second_page(request):
    return render(request, "page2.html")


class ShowAllProducts(View):

    def get(self, request):
        list_prod = Product.objects.all()
        return render(request, "table.html", {"list_prod": list_prod})


@method_decorator(login_required, name="dispatch")
class CreateOrder(View):

    def get(self, request):
        list_prod = Product.objects.all()
        return render(request, "order.html", {"list_prod": list_prod})

@method_decorator(login_required, name="dispatch")
class BuyProduct(View):

    def post(self, request, product_id: int):
        user_id = request.user
        product = get_object_or_404(Product, id=product_id)
        # prod = Product.objects.get(id=product_id)
        order_count = request.POST.get("count")
        a = Product.objects.get(id=product_id).cost
        b = Product.objects.get(id=product_id).count
        if int(order_count) <= int(b):
                order_points = (int(order_count) * int(a))
                if user_id.points >= order_points and int(b) >= int(order_count):
                    order = Order(
                        product_id=product.id,
                        user=request.user,
                        order_count=order_count,
                        order_sum=order_points,
                        )
                    order.save()
                    product.count -= int(order_count)
                    product.save(update_fields=["count"])
                    user_id.points -= int(order_points)
                    user_id.save(update_fields=["points"])
                    return redirect("profile")
        return render(request, "order.html", {"order_count": order_count})


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

    def post(self, request):
        user = request.user
        ticket_id = request.POST.get("id_ticket")
        ticket = Ticket.objects.get(id=ticket_id)
        if ticket.available:
            ticket.user_id_id = user
            ticket.available = False
            ticket.save(update_fields=["user_id_id", "available"])
            user.points += 20
            user.save(update_fields=["points"])
            return redirect("profile")
        return render(request, "usedticket.html")

class ShowTickets(View):

    def get(self, request):
        tickets_all = Ticket.objects.all()
        return render(request, "tickets.html", {"tickets_all": tickets_all})

