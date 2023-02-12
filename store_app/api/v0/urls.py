from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("product", views.ProductControlViewSet)
router.register("order", views.OrderControlViewSet)
router.register("ticket", views.TicketControlViewSet)

urlpatterns = [
    path("", include(router.urls))
]
