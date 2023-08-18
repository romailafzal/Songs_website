from rest_framework import serializers
from .models import Song, Tag, Album, Like, Favorite, Comment
from django.utils import timezone

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'

    def create(self, validated_data):
        if 'scheduled_publish_time' in validated_data and validated_data['scheduled_publish_time'] <= timezone.now():
            validated_data['is_published'] = True
        return super().create(validated_data)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
