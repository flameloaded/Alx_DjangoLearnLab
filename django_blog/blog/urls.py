from django.urls import path
from .views import UserLoginView, UserLogoutView, register, profile, home

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path('', home, name='home')
    # You can add your blog index view later, e.g., path("", views.index, name="home"),
]