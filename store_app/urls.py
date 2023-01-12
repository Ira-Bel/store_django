from django.urls import path, include
from store_app import views


urlpatterns = [
    path("", views.base_page, name="home"),
    # path("table/", views.show_products, name="list-prod"),
    path("table/", views.ShowAllProducts.as_view(), name="list_prod"),
]