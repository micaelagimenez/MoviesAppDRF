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
from rest_framework.permissions import AllowAny
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
    
# Authentication Views
class CustomRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        custom_data = {"message": "some message", "status": "ok"}
        response.data.update(custom_data)
        return response


class CustomLoginView(LoginView):
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "some message", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response
    
# CRUD Movies
class ListMovieAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ['genre']
    permission_classes = (AllowAny, )
    
class CreateMovieAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny, )

class UpdateMovieAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny, )

class DeleteMovieAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny, )
    
class DetailMovieAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny, )
    
# CRUD Characters
class ListCharactersAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer
    permission_classes = (AllowAny, )

class CreateCharactersAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (AllowAny, )

class UpdateCharactersAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (AllowAny, )

class DeleteCharactersAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (AllowAny, )
    
class DetailCharactersAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer
    permission_classes = (AllowAny, )
   
class SearchCharactersAPIView(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ['age','movie']
    permission_classes = (AllowAny, )