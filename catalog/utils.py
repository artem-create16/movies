import requests
from movies.settings import API_KEY
from pydantic import BaseModel
from typing import List


class Results(BaseModel):
    title: str
    overview: str
    vote_average: str
    release_date: str
    id: str


class Movies(BaseModel):
    page: str
    results: List[Results]


def get_movies(section, page):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{section}?api_key={API_KEY}&language=ru&page={page}'
    )
    return parse(response.json())


def search_movies(req):
    response = requests.get(
        f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={req}&language=ru'
    )
    return parse(response.json())


def get_certain_movie(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=ru'
    )
    return parse_certain(response.json())


def parse(json):
    movie = Movies(**json)
    print(movie)
    return movie.results


def parse_certain(json):
    movie = Results(**json)
    return movie
