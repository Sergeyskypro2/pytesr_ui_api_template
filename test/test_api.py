from movie import Movie
import allure


@allure.severity("blocker")
@allure.feature("ASSERT")
def test_get_movie_data():
    movie = Movie()
    body = movie.get_movie_data()
    assert body["status_code"] == 200


def test_similar_dy_id():
    similar = Movie()
    body = similar.get_similar_by_id()
    assert body["status_code"] == 200


def test_list_of_movies():
    movies = Movie()
    body = movies.get_list_of_movies()
    assert body["status_code"] == 200


def test_search_movie():
    movie = Movie()
    body = movie.search_without_keyword()
    assert body["status_code"] == 400


def test_search_staff():
    staff = Movie()
    body = staff.search_staff_without_id()
    assert body["status_code"] == 400
