from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics, permissions


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().prefetch_related("books")
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer


# --- LIST VIEW ---
# Anyone can see the list of books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()   # What data to show
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # No login required

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

    # Optional: customize behavior on save
    def perform_create(self, serializer):
        # You can add extra logic here if needed
        serializer.save()

# --- UPDATE VIEW ---
# Only authenticated users can update books
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # You could add extra checks here
        serializer.save()

# --- DELETE VIEW ---
# Only authenticated users can delete books
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
