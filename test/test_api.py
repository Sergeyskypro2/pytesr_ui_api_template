from movie import Movie
import allure


@allure.severity("blocker")
@allure.feature("ASSERT")
def test_get_movie_data():
    movie_data = Movie()
    body = movie_data.get_movie_data()
    assert body["status_code"] == 200


def test_similar_dy_id():
    similar_movies = Movie()
    body = similar_movies.get_similar_by_id()
    assert body["status_code"] == 200


def test_list_of_movies():
    list = Movie()
    body = list.get_list_of_movies()
    assert body["status_code"] == 200


def test_search_movie():
    movie = Movie()
    body = movie.search_without_keyword()
    assert body["status_code"] == 400


def test_search_staff():
    staff = Movie()
    body = staff.search_staff_without_id()
    assert body["status_code"] == 400