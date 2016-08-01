from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.http import Http404
from django.views import generic

from .models import GENRES, Movie
from .forms import MovieForm
import random
import datetime
from string import digits, ascii_uppercase
from collections import OrderedDict


class RandomView(generic.DetailView):
    template_name = 'movies/random.html'

    def get_object(self):
        movies = Movie.objects.all()
        count = movies.count()
        movies.exclude(publish=False)
        has_movies = False
        for movie in movies:
            if movie.publish:
                has_movies = True

        if count > 0 and has_movies:
            movie_ids = [movie.id for movie in movies if movie.publish]
            movie = get_object_or_404(Movie, pk=random.choice(movie_ids))
            return movie



def movies_list(request):
    movies = Movie.objects.filter(publish=True).order_by('title')
    movies.exclude(publish=False)
    letters = '#' + ascii_uppercase
    alpha_order = [[letter, []] for letter in letters]
    for movie in movies:
        first_letter = movie.title[0]
        if first_letter in list(digits):
            alpha_order[0][1].append(movie)
        else:
            for letter in range(len(alpha_order)):
                if first_letter.upper() == alpha_order[letter][0]:
                    alpha_order[letter][1].append(movie)

    return render(request, 'movies/movie_list.html', {'movies': movies, 'movie_index': alpha_order})


def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres_list = movie.genre
    movie_genres = []
    for url, name in GENRES:
        for genre in genres_list:
            if genre == url:
                movie_genres.append([name, url])

    return render(request, 'movies/movie_detail.html', {'movie': movie, 'genres': movie_genres})


def publish_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if not movie.publish:
        movie.publish = True
        movie.save()
        message = "O filme {} foi publicado com sucesso".format(movie.title)
        return render(request, 'movies/publish.html', {'movie': movie, 'message': message})
    else:
        movie.publish = False
        movie.save()
        message = "O filme {} foi omitido com sucesso".format(movie.title)
        return render(request, 'movies/publish.html', {'movie': movie, 'message': message})


def remove_movie(request, movie_pk):
    if request.user.is_superuser:
        movie = get_object_or_404(Movie, pk=movie_pk)
        movie.delete()
        return redirect('movies:movies.views.movies_list')
    else:
        return HttpResponse("Você não tem permissão para fazer isso")


def by_genre(request, genre):
    
    
    for url, name in GENRES:
        if url == genre:
            genre_title = name

    movie_list = []
    for movie in Movie.objects.all():
        for movie_genre in movie.genre:
            if movie_genre.lower() == genre.lower():
                pk = movie.pk
                movie_list.append(get_object_or_404(Movie, pk=pk))

    movie_list.sort(key=lambda x: x.title)
    return render(request, 'movies/by_genre.html', {'movie_list': movie_list, 'genre': genre_title})



def genres(request):
    genres_list = OrderedDict(GENRES)
    return render(request, 'movies/genres_list.html', {'genres_list': genres_list})


def movie_new(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.author = request.user
            movie.pub_date = timezone.now()
            movie.publish = False
            movie.save()
            return redirect('movies:movie_detail', movie_pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'movies/movie_edit.html', {'form': form})


def movie_edit(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.author = request.user
            movie.pub_date = timezone.now()
            movie.save()
            return redirect('movies:movie_detail', movie_pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_edit.html', {'form': form})
