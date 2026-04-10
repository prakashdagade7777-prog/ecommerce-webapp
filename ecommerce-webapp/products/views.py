from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductListView(generics.ListCreateAPIView):
    """
    GET  /api/products/       - List all active products
    POST /api/products/       - Create new product (auth required)
    Supports filtering by category: /api/products/?category=Electronics
    Supports search: /api/products/?search=laptop
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['price', 'created_at', 'name']

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True).select_related('category')
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name__icontains=category)
        return queryset


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/products/{id}/ - Get product details
    PUT    /api/products/{id}/ - Update product (auth required)
    DELETE /api/products/{id}/ - Delete product (auth required)
    """
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
