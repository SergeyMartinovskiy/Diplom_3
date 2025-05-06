from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import TimeoutException

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_new_page(self, url):
        self.driver.get(url)

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.driver.execute_script('arguments[0].click();', locator)


