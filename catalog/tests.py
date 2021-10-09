from unittest.mock import patch

from django.test import TestCase

from catalog.utils import (get_movies,
                           parse_video,
                           parse_certain,
                           parse_search_movies,
                           parse_movies,
                           search_movies,
                           get_certain_movie,
                           get_video)
from catalog.views import check_pagination


class Test(TestCase):
    @patch('catalog.utils.requests.get')
    def test_get_movies(self, mock_get):
        mock_get.return_value.status_code = 200
        response = get_movies(section='popular', page=1)
        self.assertEqual(response.status_code, 200)

    @patch('catalog.utils.requests.get')
    def test_get_movies_error(self, mock_get):
        mock_get.return_value.status_code = 404
        response = get_movies(
            section='non_exists',
            page=1234
        )
        self.assertEqual(response.status_code, 404)

    @patch('catalog.utils.requests.get')
    def test_search_movies(self, mock_get):
        mock_get.return_value.status_code = 200
        response = search_movies(req='Москва слезам не верит')
        self.assertEqual(response.status_code, 200)

    @patch('catalog.utils.requests.get')
    def test_get_certain_movie(self, mock_get):
        mock_get.return_value.status_code = 200
        response = get_certain_movie(movie_id=123)
        self.assertEqual(response.status_code, 200)

    @patch('catalog.utils.requests.get')
    def test_get_certain_movie_error(self, mock_get):
        mock_get.return_value.status_code = 404
        response = get_certain_movie(movie_id=0)
        self.assertEqual(response.status_code, 404)

    @patch('catalog.utils.requests.get')
    def test_get_video(self, mock_get):
        mock_get.return_value.status_code = 200
        response = get_video(title='Москва слезам не верит', year='1979')
        self.assertEqual(response.status_code, 200)

    @patch('catalog.utils.requests.get')
    def test_parse_movies(self, mock_get):
        results = {"page": "1", "results": [{"title": "Moscow",
                                             "overview": "some overview",
                                             "vote_average": "some vite_average",
                                             "release_date": "some release_date",
                                             "id": "some id"}]}
        mock_get.return_value.json.return_value = results
        response = parse_movies(section='popular', page=1)
        self.assertEqual(response, results)

    @patch('catalog.utils.requests.get')
    def test_parse_search_movies(self, mock_get):
        results = {"page": "1", "results": [{"title": "Moscow",
                                             "overview": "some overview",
                                             "vote_average": "some vite_average",
                                             "release_date": "some release_date",
                                             "id": "some id"}]}
        mock_get.return_value.json.return_value = results
        response = parse_search_movies(req='Moscow')
        self.assertEqual(response, results)

    @patch('catalog.utils.requests.get')
    def test_parse_certain(self, mock_get):
        results = {"title": "Moscow",
                   "overview": "some overview",
                   "vote_average": "some vite_average",
                   "release_date": "some release_date",
                   "id": "some id"}
        mock_get.return_value.json.return_value = results
        response = parse_certain(movie_id=123)
        self.assertEqual(response, results)

    @patch('catalog.utils.requests.get')
    def test_parse_video(self, mock_get):
        results = {"results": [{"title": "Moscow",
                                "link": "some link",
                                'material_data': {}}]}
        mock_get.return_value.json.return_value = results
        response = parse_video(title='Moscow', year='1979')
        self.assertEqual(response, results)

    @patch('catalog.utils.requests.get')
    def test_check_pagination(self, mock_get):
        mock_get.return_value.status_code = 404
        response = check_pagination(page=1001)
        self.assertEqual(response.status_code, 404)

    def test_check_popular_link(self):
        response = self.client.get('/popular/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/popular.html')
        # self.assertContains(response.content, 'Company Name XYZ')

    def test_check_top_link(self):
        response = self.client.get('/top/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/top.html')

    def test_check_now_link(self):
        response = self.client.get('/now/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/now_playing.html')

    def test_check_movie_link(self):
        response = self.client.get('/movie/739990/Ночные%20тетради/2021-09-15/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/certain_movie.html')

    def test_search_link(self):
        response = self.client.get('/search/Ночные%20тетради/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/find_films.html')
