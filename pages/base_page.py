from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_new_page(self, url):
        self.driver.get(url)

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()

    def wait_and_click_element(self, locator):
        element = WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable(locator))
        element.click()

    def close_modal_if_open(self):
        try:
            modal_close_button = WebDriverWait(self.driver, 5).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "selector_for_close_button"))
            )
            modal_close_button.click()
        except TimeoutException:
            pass

    def compare_urls(self, expected_url: str) -> bool:
        current_url = self.driver.current_url
        return current_url == expected_url

