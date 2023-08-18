from rest_framework import viewsets
from .models import Song, Tag, Album, Like, Favorite, Comment
from .serializers import SongSerializer, TagSerializer, AlbumSerializer, LikeSerializer, FavoriteSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated


class SongViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
