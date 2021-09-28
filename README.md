# Movies
## Description
Search movies by title, list of popular movies, movies watched now and top ratings
To watch a movie, click on its title
If the given results do not contain the required film, go to the end of the page, clicking on the link will redirect you to a search on the Internet
## Installation
```
git clone https://github.com/artem-create16/movies.git
cd movies
```
Fill .env.example and rename to .env
API_KEY you can get here https://www.themoviedb.org/documentation/api
API_KEY_VIDEO can get here https://kodik.cc/
```
gunicorn movies.wsgi 
```
