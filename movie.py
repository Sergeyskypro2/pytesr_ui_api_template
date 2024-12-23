import requests
from settings import VALUE, KEY


class Movie:
    def __init__(self):
        self.key = KEY
        self.value = VALUE
        self.url = "https://kinopoiskapiunofficial.tech"

    """Получение данных о фильмк"""
    def get_movie_data(self):
        headers = {
            "Key": self.key,
            "Value": self.value,
            "Content-Type": "application/json"
        }
        movie = requests.get(self.url + '/api/v2.2/films/301', headers=headers) # noqa
        return movie.json()

    """Поиск похожих фильмоф по ID"""
    def get_similar_by_id(self):
        headers = {
            "Key": self.key,
            "Value": self.value,
            "Content-Type": "application/json"
        }
        movies = requests.get(self.url + '/api/v2.2/films/301/similars', headers=headers) # noqa
        return movies.json()

    """Получить список фильмов"""
    def get_list_of_movies(self):
        headers = {
            "Key": self.key,
            "Value": self.value,
            "Content-Type": "application/json"
        }
        movies = requests.get(self.url + '/api/v2.2/films/collections', headers=headers) # noqa
        return movies.json()

    """Поиск фильма без ключевого слова"""
    def search_without_keyword(self):
        headers = {
            "Key": self.key,
            "Value": self.value,
            "Content-Type": "application/json"
        }
        movies = requests.get(self.url + '/api/v2.1/films/search-by-keyword', headers=headers) # noqa
        return movies.json()

    """Поиск персонажа без ID"""
    def search_staff_without_id(self):
        headers = {
            "Key": self.key,
            "Value": self.value,
            "Content-Type": "application/json"
        }
        movies = requests.get(self.url + '/api/v1/staff', headers=headers) # noqa
        return movies.json()
