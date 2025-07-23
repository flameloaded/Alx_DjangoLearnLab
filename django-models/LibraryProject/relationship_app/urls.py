from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view
from .views import profile_view
urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-role/', admin_view, name='admin-role'),
    path('librarian-role/', librarian_view, name='librarian-role'),
    path('member-role/', member_view, name='member-role'),
    path('profile/', profile_view, name='profile'),
]


