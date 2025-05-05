import pytest
from selenium import webdriver
from pages.courses_page import CoursesPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_filter_reduces_counts(driver):

    page = CoursesPage(driver)
    page.driver.get("https://skillbox.ru/code")

    initial_prof, initial_courses = page.get_counts()
    page.apply_filter("backend")

    new_prof, new_courses = page.get_counts()
    assert new_prof < initial_prof, "Фильтр не уменьшил кол-во профессий"
    assert new_courses < initial_courses, "Фильтр не уменьшил кол-во курсов"

def test_filter_navigation(driver):

    page = CoursesPage(driver)
    page.driver.get("https://skillbox.ru/code")
    page.apply_filter("web")
    assert page.is_url_contains("web"), "URL не соответствует фильтру"

