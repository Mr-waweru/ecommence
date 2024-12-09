from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, OrderSerializer
from products.models import Product, Category
from orders.models import Order
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

User = get_user_model()

class UserViewSet(ReadOnlyModelViewSet):
    """ViewSet for listing or retrieving users (read-only)."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(ModelViewSet):
    """ViewSet for managing products."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]    # Authenticated users can create/update; everyone can read


class CategoryViewSet(ModelViewSet):
    """ViewSet for managing categories."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderViewSet(ModelViewSet):
    """ViewSet for managing orders."""
    queryset = Order.objects.select_related('product', 'created_by')  # Optimize queryset
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access