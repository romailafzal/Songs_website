from .models import Song
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'song_name', 'song_artist', 'song_album', 'song_genre', 'song_year']