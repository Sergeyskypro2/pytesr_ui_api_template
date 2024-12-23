from MainPage import MainPage
from search import Search
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

    with allure.step("Нажать на поиск и ввести название на кирилице"):
        search_page = Search(browser)
        search_page.search_in_Cyrillic("Прометей")
        url = browser.current_url
        print(url)

    with allure.step("Нажать на поиск и ввести цифры"):
        search_page = Search(browser)
        search_page.search_by_numbers("2012")

    with allure.step("Нажать на Кинопоиск"):
        main_page = Search(browser)
        main_page.main_page()

    with allure.step("Нажать на вкладку буду смотреть"):
        watch = Search(browser)
        watch.watch()

    with allure.step("Закрыть браузер"):
        browser.quit()