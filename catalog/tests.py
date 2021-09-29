from django.test import TestCase
from catalog.forms import FindMovies
from catalog.utils import get_movies, search_movies, get_certain_movie, get_video


class Test(TestCase):
    def test_check_popular_link(self):
        response = self.client.get('/popular/1/')
        self.assertEqual(response.status_code, 200)

    def test_check_top_link(self):
        response = self.client.get('/top/1/')
        self.assertEqual(response.status_code, 200)

    def test_check_movie_link(self):
        response = self.client.get('/movie/739990/Ночные%20тетради/2021-09-15/')
        self.assertEqual(response.status_code, 200)

    def test_search_link(self):
        response = self.client.get('/search/Ночные%20тетради/')
        self.assertEqual(response.status_code, 200)

    def test_form_find_movies(self):
        form_data = {'something': 'something'}
        form = FindMovies(data=form_data)
        self.assertTrue(form.is_valid())

    def test_get_movies(self):
        movies = get_movies(section='popular', page='1')
        self.assertTrue(movies.results is not None)

    def test_search_movies(self):
        movies = search_movies(req='Москва слезам не верит')
        self.assertTrue(movies.results is not None)

    def test_get_certain_movie(self):
        movie = get_certain_movie(movie_id=123)
        self.assertTrue(movie is not None)

    def test_get_video(self):
        video = get_video(title='Москва слезам не верит', year='1980')
        self.assertTrue(video is not None)

