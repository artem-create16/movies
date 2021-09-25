from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from catalog.utils import get_popular_movies


def index(request):
    return render(request, 'catalog/index.html', {'movies': get_popular_movies("popular")})


def top(request):
    return render(request, 'catalog/top.html', {'movies': get_popular_movies("top_rated")})


def now_playing(request):
    return render(request, 'catalog/now_playing.html', {'movies': get_popular_movies("now_playing")})
