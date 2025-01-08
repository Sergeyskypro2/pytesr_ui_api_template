from movie import Movie
import allure


@allure.severity("blocker")
@allure.feature("ASSERT")
def test_get_movie_data():
    movie = Movie()
    resp = movie.get_movie_data()
    assert resp["status_code"] == 200


def test_similar_dy_id():
    similar = Movie()
    resp = similar.get_similar_by_id()
    assert resp["status_code"] == 200


def test_list_of_movies():
    movies = Movie()
    resp = movies.get_list_of_movies()
    assert resp["status_code"] == 200


def test_search_movie():
    movie = Movie()
    resp = movie.search_without_keyword()
    assert resp["status_code"] == 400


def test_search_staff():
    staff = Movie()
    resp = staff.search_staff_without_id()
    assert resp["status_code"] == 400
