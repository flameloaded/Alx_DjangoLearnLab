from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView  # required exact import
from .models import Book
from .models import Library  # required exact import
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # ✅ Add this
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import UserProfile
from django.shortcuts import render


from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import UserProfile

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


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
            return redirect('list_books')  # Change to your desired post-login page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})






@login_required
def profile_view(request):
    profile = request.user.userprofile  # Access related UserProfile directly
    return render(request, 'relationship_app/profile.html', {'profile': profile})
