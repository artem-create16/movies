from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from catalog.utils import get_movies, search_movies
from .forms import FindMovies


def index(request):
    form = FindMovies()
    if request.method == 'GET':
        form = FindMovies(request.GET)
        if form.is_valid() and form.cleaned_data['movies'] != '':
            value = form.cleaned_data.get('movies')
            return redirect('search', value)
    return render(request, 'catalog/index.html', {'movies': get_movies("popular"), 'form': form})


def top(request):
    return render(request, 'catalog/top.html', {'movies': get_movies("top_rated")})


def now_playing(request):
    return render(request, 'catalog/now_playing.html', {'movies': get_movies("now_playing")})


def show_find_movies(request, movie):
    print(movie)
    return render(request, 'catalog/find_films.html', {'movies': search_movies(movie)})

