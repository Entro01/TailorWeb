# shop/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product, Fabric, Cart, CartItem, Order, OrderItem, UserProfile
from .serializers import ProductSerializer, FabricSerializer, CartSerializer, OrderSerializer, UserProfileSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def products(self, request):
        name = request.query_params.get('name')
        if name:
            queryset = Product.objects.filter(name__icontains=name)
        else:
            queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class FabricViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fabric.objects.all()
    serializer_class = FabricSerializer

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)

    @action(detail=True, methods=['put'])
    def add_item(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        product = Product.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

    def create(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user).last()
        if not cart:
            return Response({'error': 'Cart is empty'}, status=400)
        total_amount = sum(item.product.price * item.quantity for item in cart.items.all())
        order = Order.objects.create(user=user, total_amount=total_amount)
        for item in cart.items.all():
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart.delete()
        serializer = self.get_serializer(order)
        return Response(serializer.data)

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        user = self.request.user
        return UserProfile.objects.filter(user=user)