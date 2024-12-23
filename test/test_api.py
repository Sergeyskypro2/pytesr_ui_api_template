from movie import Movie
import allure


@allure.severity("blocker")
@allure.feature("ASSERT")
def test_get_movie_data():
    movie_data = Movie()
    body = movie_data.get_movie_data()
    # assert body.status_code == 200
    print(body)


def test_similar_dy_id():
    similar_movies = Movie()
    body = similar_movies.get_similar_by_id()
    print(body)


def test_list_of_movies():
    list = Movie()
    body = list.get_list_of_movies()
    print(body)


def test_search_movie():
    movie = Movie()
    boby = movie.search_without_keyword()
    print(boby)


def test_search_staff():
    staff = Movie()
    body = staff.search_staff_without_id()
    print(body)