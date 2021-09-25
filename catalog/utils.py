import requests
from movies.settings import API_KEY
from pydantic import BaseModel
from typing import List


class Results(BaseModel):
    title: str
    overview: str
    vote_average: str
    release_date: str


class Movies(BaseModel):
    page: str
    results: List[Results]


def get_movies(section):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{section}?api_key={API_KEY}&language=ru&page=1'
    )
    return parse(response.json())


def search_movies(req):
    response = requests.get(
        f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={req}&language=ru'
    )
    return parse(response.json())


def parse(json):
    movie = Movies(**json)
    return movie
