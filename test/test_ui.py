from MainPage import MainPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import allure


@allure.severity("blocker")
@allure.feature("ASSERT")
def test_mane_page():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # noqa
    browser.implicitly_wait(20)
    browser.maximize_window()
    browser.execute_script("document.body.style.zoom='80%'")

    with allure.step("Открыть сайт"):
        main_page = MainPage(browser)
        main_page.go()
        url = main_page.current_url
        assert url == "https://www.kinopoisk.ru/"

    with allure.step("Нажать на поиск и ввести название на кирилице"):
        search_page = MainPage(browser)
        search_page.search_in_Cyrillic("Прометей")
        url = search_page.current_url
        assert url == "https://www.kinopoisk.ru/index.php?kp_query=Прометей"

    with allure.step("Нажать на поиск и ввести цифры"):
        search_page = MainPage(browser)
        search_page.search_by_numbers("2012")
        url = search_page.current_url
        assert url == "https://www.kinopoisk.ru/index.php?kp_query=2012"

    with allure.step("Нажать на Кинопоиск"):
        main_page = MainPage(browser)
        main_page.main_page()
        url = main_page.current_url
        assert url == "https://www.kinopoisk.ru/"

    with allure.step("Нажать на вкладку расширенный поиск"):
        watch = MainPage(browser)
        watch.watch()
        url = watch.current_url
        assert url == "https://www.kinopoisk.ru/s/"

    with allure.step("Закрыть браузер"):
        browser.quit()