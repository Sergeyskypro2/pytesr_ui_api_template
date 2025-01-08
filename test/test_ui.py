from MainPage import MainPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import allure


@allure.severity("blocker")
@allure.feature("ASSERT")
def test_mane_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # noqa
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='80%'")

    with allure.step("Открыть сайт"):
        main_page = MainPage(driver)
        main_page.go()
        url = driver.current_url
        assert url == "https://www.kinopoisk.ru/"

    with allure.step("Нажать на поиск и ввести название на кирилице"):
        search_page = MainPage(driver)
        search_page.search_in_Cyrillic("Прометей")
        url = driver.current_url
        assert url == "https://www.kinopoisk.ru/index.php?kp_query=%D0%9F%D1%80%D0%BE%D0%BC%D0%B5%D1%82%D0%B5%D0%B9" # noqa

    with allure.step("Нажать на поиск и ввести цифры"):
        search_page = MainPage(driver)
        search_page.search_by_numbers("2012")
        url = driver.current_url
        assert url == "https://www.kinopoisk.ru/index.php?kp_query=2012"

    with allure.step("Нажать на Кинопоиск"):
        main_page = MainPage(driver)
        main_page.main_page()
        url = driver.current_url
        assert url == "https://www.kinopoisk.ru"

    with allure.step("Нажать на вкладку расширенный поиск"):
        watch = MainPage(driver)
        watch.watch()
        url = driver.current_url
        assert url == "https://www.kinopoisk.ru/s"

    with allure.step("Закрыть браузер"):
        driver.quit()
