from django.urls import path
from .views import UserLoginView, UserLogoutView, register, profile, home
from .views import( PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, 
                   CommentCreateView, 
                   CommentUpdateView,
                    CommentDeleteView,
                    PostsByTagView, search)


urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'), 
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
     # Tags
    path('tags/<slug:slug>/', PostsByTagView.as_view(), name='posts-by-tag'),

    # Optional dedicated search endpoint (you can also use /?q=...)
    path('search/', search, name='search'),
]