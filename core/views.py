from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import *
from .models import *
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAdminUser
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
    
# Authentication Views
class CustomRegisterView(RegisterView):
    """This endpoint allows User to register"""
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        custom_data = {"message": "some message", "status": "ok"}
        response.data.update(custom_data)
        return response


class CustomLoginView(LoginView):
    """This endpoint allows User to Login"""
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "some message", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response
    
# CRUD Movies
class ListMovieAPIView(ListAPIView):
    """This endpoint lists all of the available movies from the database"""
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    permission_classes = (AllowAny, )
    
class CreateMovieAPIView(CreateAPIView):
    """This endpoint allows to create a movie"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny, )

class UpdateMovieAPIView(UpdateAPIView):
    """This endpoint allows to update a specific movie given its id"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny, )

class DeleteMovieAPIView(DestroyAPIView):
   """This endpoint allows to delete a specific movie given its id"""
   queryset = Movie.objects.all()
   serializer_class = MovieSerializer
   permission_classes = (AllowAny, )
    
class DetailMovieAPIView(ListAPIView):
    """This endpoint shows the detail of a movie given its id"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny, )
    
# CRUD Characters
class ListCharactersAPIView(ListAPIView):
    """This endpoint lists all of the available characters from the database"""
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer
    permission_classes = (AllowAny, )

class CreateCharactersAPIView(CreateAPIView):
    """This endpoint allows to create a character"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (AllowAny, )

class UpdateCharactersAPIView(UpdateAPIView):
    """This endpoint allows to update a specific character given its id"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (AllowAny, )

class DeleteCharactersAPIView(DestroyAPIView):
    """This endpoint allows to delete a specific character given its id"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (AllowAny, )
    
class DetailCharactersAPIView(ListAPIView):
    """This endpoint shows the detail of a character given its id"""
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer
    permission_classes = (AllowAny, )

# Searches
class SearchCharactersAPIView(ListAPIView):
    """This endpoint allows to search for any character in the database"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ['age','movie']
    permission_classes = (AllowAny, )
    
class SearchMovieAPIView(ListAPIView):
    """This endpoint allows to search for any movie in the database"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ['genre']
    permission_classes = (AllowAny, )