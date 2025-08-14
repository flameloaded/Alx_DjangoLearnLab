from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from django_filters import rest_framework 



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().prefetch_related("books")
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer


# --- LIST VIEW ---
# Anyone can view all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()   # What data to show
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # No login required

    # Enable filtering, searching, and ordering
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # 1. Filtering fields (exact matches)
    filterset_fields = ['title', 'author__name', 'publication_year']

    # 2. Searching fields (partial matches)
    search_fields = ['title', 'author__name']

    # 3. Ordering fields (sorting)
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

# --- DETAIL VIEW ---
# Anyone can view details of a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# --- CREATE VIEW ---
# Only authenticated users can add new books
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

# --- UPDATE VIEW ---
# Only authenticated users can update books
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

# --- DELETE VIEW ---
# Only authenticated users can delete books
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]



