from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, TagViewSet, AlbumViewSet, LikeViewSet, FavoriteViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='song')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'albums', AlbumViewSet, basename='album')
router.register(r'likes', LikeViewSet, basename='like')
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]