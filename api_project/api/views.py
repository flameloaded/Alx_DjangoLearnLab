# api/views.py
from rest_framework import generics,viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]




"""
BookViewSet handles CRUD operations for books.
Authentication: Token-based authentication (DRF TokenAuthentication)
Permissions: Custom IsAdminOrReadOnly — anyone can read, only admins can write.
"""