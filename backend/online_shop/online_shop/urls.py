# shop/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'fabrics', views.FabricViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'profiles', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),]