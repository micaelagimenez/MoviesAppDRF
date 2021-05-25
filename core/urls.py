from django.urls import path
from core import views
from core.views import *

urlpatterns = [
    path('register', CustomRegisterView.as_view(), name="register"),
    path('login', CustomLoginView.as_view(), name="login"),
    path("movies",views.ListMovieAPIView.as_view(),name="movie_list"),
    path("movie/create/", views.CreateMovieAPIView.as_view(),name="movie_create"),
    path("movie/<int:pk>/", views.DetailMovieAPIView.as_view(),name="movie_detail"),
    path("movies/search/", views.SearchMoviesAPIView.as_view(),name="movies_search"),
    path("movie/item/<int:pk>/",views.UpdateDeleteMovieAPIView.as_view(),name="update_movie"),
    path("characters",views.ListCharactersAPIView.as_view(),name="characters_list"),
    path("character/<int:pk>",views.DetailCharactersAPIView.as_view(),name="characters_detail"),
    path("characters/search/", views.SearchCharactersAPIView.as_view(),name="characters_search"),
    path("characters/create/", views.CreateCharactersAPIView.as_view(),name="characters_create"),
    path("characters/item/<int:pk>/",views.UpdateDeleteCharactersAPIView.as_view(),name="characters_movie")
]