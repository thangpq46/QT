from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'product', ProductViewSet,basename="product")
router.register(r'category', CategoryViewSet,basename="category")
router.register(r'pricing', PricingViewSet,basename="pricing")
router.register(r'Order', OrderViewSet,basename="order")
router.register(r'Orderdetails', OrderdetailsViewSet,basename="orderdetails")
urlpatterns = router.urls