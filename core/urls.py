from django.urls import path
from core import views
from core.views import *

urlpatterns = [
    path('register', CustomRegisterView.as_view()),
    path('login', CustomLoginView.as_view()),
    path("movies",views.ListMovieAPIView.as_view(),name="movie_list"),
    path("movie/create/", views.CreateMovieAPIView.as_view(),name="movie_create"),
    path("movie/<int:pk>/", views.DetailMovieAPIView.as_view(),name="movie_detail"),
    path("movie/update/<int:pk>/",views.UpdateMovieAPIView.as_view(),name="update_movie"),
    path("movie/delete/<int:pk>/",views.DeleteMovieAPIView.as_view(),name="delete_movie"),
    path("characters",views.ListCharactersAPIView.as_view(),name="characters_list"),
    path("character/<int:pk>",views.DetailCharactersAPIView.as_view(),name="characters_detail"),
    path("characters/search/", views.SearchCharactersAPIView.as_view(),name="characters_search"),
    path("characters/create/", views.CreateCharactersAPIView.as_view(),name="characters_create"),
    path("characters/update/<int:pk>/",views.UpdateCharactersAPIView.as_view(),name="characters_movie"),
    path("characters/delete/<int:pk>/",views.DeleteCharactersAPIView.as_view(),name="characters_movie")
]