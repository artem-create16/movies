from django.test import TestCase
from catalog.forms import FindMovies
from catalog.utils import get_movies, search_movies, get_certain_movie, get_video
import requests_mock
from unittest.mock import patch
from catalog.utils import Movies

class Test(TestCase):
    # def test_check_for_a_non_existent_link(self):
    #     response = self.client.get('/non_exists/')
    #     self.assertEqual(response.status_code, 404)
    #
    # def test_check_unknown_category(self):
    #     response = self.client.get('127.0.0.1:8000/unknown_category/1/')
    #     self.assertEqual(response.status_code, 404)
    #
    # def test_check_page_out_of_range(self):
    #     response = self.client.get('/popular/1001/')
    #     self.assertEqual(response.status_code, 404)
    #
    # def test_check_popular_link(self):
    #     response = self.client.get('/popular/1/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'catalog/popular.html')
    #
    # def test_check_top_link(self):
    #     response = self.client.get('/top/1/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'catalog/top.html')
    #
    # def test_check_now_link(self):
    #     response = self.client.get('/now/1/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'catalog/now_playing.html')
    #
    # def test_check_movie_link(self):
    #     response = self.client.get('/movie/739990/Ночные%20тетради/2021-09-15/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'catalog/certain_movie.html')
    #
    # def test_search_link(self):
    #     response = self.client.get('/search/Ночные%20тетради/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'catalog/find_films.html')
    #
    # def test_form_find_movies(self):
    #     form_data = {'something': 'something'}
    #     form = FindMovies(data=form_data)
    #     self.assertTrue(form.is_valid())
    #
    # def test_get_movies(self):
    #     movies = get_movies(section='popular', page='1')
    #     self.assertTrue(movies.results is not None)
    #
    # def test_search_movies(self):
    #     movies = search_movies(req='Москва слезам не верит')
    #     self.assertTrue(movies.results is not None)
    #
    # def test_get_certain_movie(self):
    #     movie = get_certain_movie(movie_id=123)
    #     self.assertTrue(movie is not None)
    #
    # def test_get_video(self):
    #     video = get_video(title='Москва слезам не верит', year='1980')
    #     self.assertTrue(video is not None)

    @patch('catalog.utils.requests.get')
    def test_fuck(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json = Movies(page=1, results=[{'title': 'title',
                                                              'overview': 'overview',
                                                              'vote_average': 'vote_average',
                                                              'release_date': 'release_date',
                                                              'id': 'id'}])
        response = get_movies('popular', 1)
        self.assertEqual(response.status_code, 200)



