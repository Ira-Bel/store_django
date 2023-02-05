from django.urls import path, include
from store_app import views


urlpatterns = [
    path("", views.base_page, name="home"),
    path("orders/", views.ShowOrder.as_view(), name="orders"),
    path("tickets/", views.ShowTickets.as_view(), name="tickets"),
    path("profile", views.Profile.as_view(), name="profile"),
    path("order/", views.CreateOrder.as_view(), name="order"),
    path("table/", views.ShowAllProducts.as_view(), name="list_prod"),
    path("next/", views.second_page, name="home2"),
    # path("create/", views.CreateOrder.as_view(), name="create-order"),
]