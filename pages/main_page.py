import time

import allure
from urls import Main_URL
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    @allure.title('Открыть стартовую страницу Стелла Бургер')
    def open_start_window(self):
        pass

    @allure.title('Нажать на кнопку Личный кабинет в шапке страницы')
    def click_personal_account_button(self):
        self.close_modal_if_open()
        self.wait_and_click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.title('Перетащить булочку в корзину заказа')
    def add_bun_to_order_busket(self):
        bun_element = self.wait_and_find_element(MainPageLocators.FLUOR_BUN_BUTTON)
        basket_element = self.wait_and_find_element(MainPageLocators.ORDER_BUSKET)
        self.close_modal_if_open()
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(bun_element, basket_element).perform()
        timeout = 20 if "firefox" in self.driver.capabilities['browserName'].lower() else 10
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(MainPageLocators.COUNT_FLUOR_BUN_AFTER_ADD))
        time.sleep(2)




