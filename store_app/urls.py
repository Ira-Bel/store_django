from django.urls import path, include
from store_app import views


urlpatterns = [
    path("", views.base_page, name="home"),
    # path("table/", views.show_products, name="list-prod"),
    path("table/", views.ShowAllProducts.as_view(), name="list_prod"),
    path("next/", views.second_page, name="home2"),
    path("create/", views.CreateOrder.as_view(), name="create-order"),
]