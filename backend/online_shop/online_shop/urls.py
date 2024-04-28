# online_shop/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shop import views as shop_views

router = routers.DefaultRouter()
router.register(r'api/products', shop_views.ProductViewSet)
router.register(r'api/fabrics', shop_views.FabricViewSet)
router.register(r'api/cart', shop_views.CartViewSet)
router.register(r'api/orders', shop_views.OrderViewSet)
router.register(r'api/profiles', shop_views.UserProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('shop.urls')),  # Include the shop app URLs for user authentication
    path('api/', include(router.urls)),
]

# shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]