from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    return Response({
        'message': 'Welcome to the E-Commerce API',
        'endpoints': {
            'products': request.build_absolute_uri('/api/products/'),
            'categories': request.build_absolute_uri('/api/products/categories/'),
            'orders': request.build_absolute_uri('/api/orders/'),
            'register': request.build_absolute_uri('/api/auth/register/'),
            'login': request.build_absolute_uri('/api/auth/login/'),
            'token_refresh': request.build_absolute_uri('/api/auth/token/refresh/'),
            'profile': request.build_absolute_uri('/api/auth/profile/'),
            'admin': request.build_absolute_uri('/admin/'),
        }
    })


urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/auth/', include('users.urls')),
]
