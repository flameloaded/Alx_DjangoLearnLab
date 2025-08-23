from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path("feed/", FeedView.as_view(), name="feed"),
    path('<int:pk>/like/', views.LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', views.UnlikePostView.as_view(), name='unlike-post'),
]
urlpatterns = router.urls
