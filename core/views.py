from django.shortcuts import render
from .serializers import *
from .models import *
from django.db.models import Q

from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend

    
# Authentication Views
class CustomRegisterView(RegisterView):
    """This endpoint allows User to register"""
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        custom_data = {"message": "User created", "status": "success"}
        response.data.update(custom_data)
        return response


class CustomLoginView(LoginView):
    """This endpoint allows User to Login"""
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "User logged in", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response
    
# CRUD Movies
class ListMovieAPIView(ListAPIView):
    """This endpoint lists all of the available movies from the database"""
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    permission_classes = (IsAuthenticated, )
    
class CreateMovieAPIView(CreateAPIView):
    """This endpoint allows to create a movie"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, )

class UpdateDeleteMovieAPIView(UpdateAPIView, DestroyAPIView):
    """This endpoint allows to update or delete a specific movie given its id"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, )
    
class DetailMovieAPIView(ListAPIView):
    """This endpoint shows the detail of a movie given its id"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, )
    
# CRUD Characters
class ListCharactersAPIView(ListAPIView):
    """This endpoint lists all of the available characters from the database"""
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer
    permission_classes = (IsAuthenticated, )

class CreateCharactersAPIView(CreateAPIView):
    """This endpoint allows to create a character"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (IsAuthenticated, )

class UpdateDeleteCharactersAPIView(UpdateAPIView, DestroyAPIView):
    """This endpoint allows to update or delete a specific character given its id"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (IsAuthenticated, )
    
class DetailCharactersAPIView(ListAPIView):
    """This endpoint shows the detail of a character given its id"""
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer
    permission_classes = (IsAuthenticated, )

# Searches
class SearchCharactersAPIView(ListAPIView):
    """This endpoint allows to search for any character in the database"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, ]
    search_fields = ['name']
    filter_fields = ['age','movies']
    permission_classes = (IsAuthenticated, )
    
class SearchMoviesAPIView(ListAPIView):
    """This endpoint allows to search for any movie in the database"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    filterset_fields = ['genre']
    ordering_fields = ['creation_date']
    permission_classes = (IsAuthenticated, )
