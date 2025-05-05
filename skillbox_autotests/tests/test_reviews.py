import pytest
from selenium import webdriver
from pages.reviews_page import ReviewsPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_reviews_page_loaded(driver):

    page = ReviewsPage(driver)
    page.load()
    assert page.is_loaded(), "Страница не загрузилась"
    assert page.get_reviews_count() > 0, "Нет отзывов на странице"