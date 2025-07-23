from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView  # required exact import
from .models import Book
from .models import Library  # required exact import
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # ✅ Add this
from django.views.generic.detail import DetailView
from .models import Library, Book

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()  # required pattern
    return render(request, 'relationship_app/list_books.html', {'books': books})  # required pattern

# Class-Based View: Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Change to your desired post-login page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})




