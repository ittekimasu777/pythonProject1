from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory
from .base_page import BasePage

class CoursesPage(BasePage, PageFactory):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "filter_backend": ('CSS', 'button[data-id="backend"]'),
        "professions_count": ('XPATH', '//div[@class="professions-count"]'),
        "courses_count": ('XPATH', '//div[@class="courses-count"]'),
        "visible_courses": ('CSS', '.course-card'),
    }

    def apply_filter(self, filter_name: str):

        filter_button = getattr(self, f"filter_{filter_name.lower()}")
        filter_button.click()
        self.wait.until(lambda _: len(self.visible_courses) > 0)

    def get_counts(self) -> tuple[int, int]:

        return (
            int(self.professions_count.text),
            int(self.courses_count.text),
        )
