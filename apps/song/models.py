from django.db import models
from apps.autth.models import User
from django.utils import timezone


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    scheduled_publish_time = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag')


    def can_publish(self):
        if self.scheduled_publish_time is not None:
            return timezone.now() >= self.scheduled_publish_time
        return False

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    is_public = models.BooleanField(default=False)
    songs = models.ManyToManyField(Song, related_name='albums')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.song}'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.song}'
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.song}'