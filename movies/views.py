from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import GENRES

from django.utils import timezone


import random
from movies.models import Movie


def random_movie(request):
    count = Movie.objects.all().count()

    if count > 0:
        movie_ids = [movie.id for movie in Movie.objects.all()]
        movie = get_object_or_404(Movie, pk=random.choice(movie_ids))
        movie_poster_name = "movies/images/" + str(movie.poster.__str__().split('/')[-1])
        return render(request, 'movies/random.html', {'movie': movie, 'movie_poster': movie_poster_name})
    else:
        return HttpResponse(content="No movies in db")


def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    return render(request, 'movies/movie_detail.html', {'movie':movie})


def by_genre(request, genre):
    movie_list = []

    for movie in Movie.objects.all():
        for movie_genre in movie.genre:
            if movie_genre.lower() == genre.lower():
                pk = movie.pk
                movie_list.append(get_object_or_404(Movie, pk=pk))
    if movie_list:
        movie_list.sort(key=lambda x: x.title)
        return render(request, 'movies/by_genre.html', {'movie_list': movie_list, 'genre': genre})
    else:
        return HttpResponse(content="No movies in {} genre".format(genre), status=404 )


def genres(request):
    genres_list = []
    for genre in range(len(GENRES)):
        genres_list.append(GENRES[genre][1])
    return render(request, 'movies/genres_list.html', {'genres_list': genres_list})

