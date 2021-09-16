from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from catalog.utils import get_popular_movies


def index(request):
    template = loader.get_template('catalog/index.html')
    return render(request, 'catalog/index.html', {'movies': get_popular_movies()})
