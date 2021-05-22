from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField
from django.db.models.fields.files import ImageField

from django.contrib.auth import get_user_model

User = get_user_model()

class Character(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    story = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    creation_date = models.DateField(auto_now=True)
    rating = models.IntegerField()
    characters = models.ManyToManyField(Character, blank=True, related_name='movies') 
    
    def __str__(self):
        return self.title

class Genre(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=150)
    movies = models.ManyToManyField(Movie, related_name='genre')
    
    def __str__(self):
        return self.name