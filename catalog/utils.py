import requests
from movies.settings import API_KEY, API_KEY_VIDEO
from pydantic import BaseModel
from typing import List, Optional


class Results(BaseModel):
    title: str
    overview: str
    vote_average: str
    release_date: str
    id: str


class Movies(BaseModel):
    page: str
    results: List[Results]


class ResultsVideo(BaseModel):
    title: str
    link: str
    material_data: Optional[dict] = None


class Video(BaseModel):
    results: List[ResultsVideo]


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


def get_video(title, year):
    year = year.split('-')[0]
    title = '%20'.join(title.split())
    response = requests.get(
        f'https://kodikapi.com/search?token={API_KEY_VIDEO}&title={title}&with_material_data=true&limit=10'
    )
    return parse_video(response.json())


def parse(json):
    movie = Movies(**json)
    return movie


def parse_certain(json):
    movie = Results(**json)
    return movie


def parse_video(json):
    video = Video(**json)
    return video.results
