from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Old ListAPIView endpoint
    path('books/', BookList.as_view(), name='book-list'),
    path('auth-token/', obtain_auth_token, name='api_token_auth'),
    # All CRUD routes for BookViewSet
    path('', include(router.urls)),
]
