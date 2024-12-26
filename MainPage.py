from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.kinopoisk.ru/"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    """Поиск на кирилице"""
    def search_in_Cyrillic(self, movie: str):
        self.__driver.find_element(By.CSS_SELECTOR, "input.styles_inputActive__ICcod.styles_input__4vNAb.kinopoisk-header-search-form-input__input").send_keys(movie) # noqa
        self.__driver.find_element(By.CSS_SELECTOR, "button.styles_root__CUh_v.styles_submit__2AIpj").click() # noqa

    """Поиск с помощью цифр"""
    def search_by_numbers(self, movie: int):
        self.__driver.find_element(By.CSS_SELECTOR, "input.UnxoJ4nUSkuPXF9CyGhq.kinopoisk-header-search-form-input__input").send_keys(movie) # noqa
        self.__driver.find_element(By.CSS_SELECTOR, "button.gq5GztMRY87mAaGXPl0A.GYeMayLu5xyRrkpS3tK3").click() # noqa

    """Переход на главную страницу"""
    def main_page(self):
        self.__driver.find_element(By.CSS_SELECTOR, ".msMehWzmLAVwfQcmxv8w.uW96Br00hFkFKc_Vc7HM").click() # noqa

    """Переход в расширенный поиск"""
    def watch(self):
        self.__driver.find_element(By.CSS_SELECTOR, ".styles_advancedSearchIconActive__4bcK9.styles_advancedSearchIcon__Zxjax").click() # noqa