from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView  # required exact import
from .models import Book
from .models import Library  # required exact import

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()  # required pattern
    return render(request, 'relationship_app/list_books.html', {'books': books})  # required pattern

# Class-Based View: Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
