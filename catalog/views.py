from django.shortcuts import redirect
from django.shortcuts import render

from catalog.utils import get_movies, search_movies, get_certain_movie, get_video
from .forms import FindMovies


def main(request):
    form = FindMovies()
    if request.method == 'POST':
        form = FindMovies(request.POST)
        if form.is_valid() and form.cleaned_data['movies'] != '':
            movie = form.cleaned_data.get('movies')
            return redirect('search', movie)
    return render(request, 'catalog/main.html', {'form': form})


def popular(request, page=1):
    return render(request, 'catalog/popular.html',
                  {'movies': get_movies("popular", page=page),
                   'pages': [i for i in range(1, 100)]})


def top(request, page=1):
    return render(request, 'catalog/top.html', {'movies': get_movies("top_rated", page=page),
                                                'pages': [i for i in range(1, 100)]})


def now_playing(request, page=1):
    return render(request, 'catalog/now_playing.html', {'movies': get_movies("now_playing", page=page),
                                                        'pages': [i for i in range(1, 100)]})


def show_find_movies(request, movie):
    return render(request, 'catalog/find_films.html', {'movies': search_movies(movie)})


def show_certain_movie(request, id, title, year):
    return render(request, 'catalog/certain_movie.html', {'movie': get_certain_movie(id), 'video': get_video(title, year)})
