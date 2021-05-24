from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    
    class Meta:
        model = Movie
        fields = ('title', 'image', 'rating', 'characters', 'genre')
        extra_kwargs = {'image': {'required': False, 'allow_null': True}}    
        
class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title', 'image', 'creation_date')
        extra_kwargs = {'image': {'required': False, 'allow_null': True}}   
        
class CharacterSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), many=True)
    
    class Meta: 
        model = Character
        fields = ['name', 'age', 'image', 'movies', 'story']
        extra_kwargs = {'image': {'required': False, 'allow_null': True}}
        
class CharacterListSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Character
        fields = ['name', 'image']
        extra_kwargs = {'image': {'required': False, 'allow_null': True}}
        
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Genre
        fields = ['name','movies']
        