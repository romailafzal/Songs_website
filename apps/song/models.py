from django.db import models

# Create your models here.
class Song(models.Model):
    song_name = models.CharField(max_length=100)
    song_artist = models.CharField(max_length=100)
    song_album = models.CharField(max_length=100)
    song_genre = models.CharField(max_length=100)
    song_year = models.IntegerField()

    def __str__(self):
        return self.song_name