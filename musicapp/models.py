from ast import Delete
from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.CharField(max_length = 30)


class Lyric(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    content = models.TextField(null = False, blank = True)
    song_id = models.CharField(max_length = 30)

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    Lyric = models.ForeignKey(Lyric)
    title = models.CharField(max_length = 100)
    date_released = models.DateField(null = True, blank = True)
    likes = models.CharField(max_length = 30)
    artiste_id = models.CharField(max_length = 30)
# Create your models here.
