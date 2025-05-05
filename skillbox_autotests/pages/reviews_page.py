from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ReviewsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self) -> bool:

        return len(self.driver.find_elements(By.XPATH, '//div[@class="reviews-list"]')) > 0

    def load(self):

        self.driver.get("https://skillbox.ru/otzyvy/?direction=code")
        self.wait.until(lambda _: self.is_loaded())

    def get_reviews_count(self) -> int:

        return len(self.driver.find_elements(By.XPATH, '//div[@class="review-item"]'))
