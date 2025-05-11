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
        action_chains = ActionChains(self.driver)
        action_chains.click_and_hold(bun_element).pause(1).move_to_element(basket_element).pause(1).release().perform()

    @allure.step("Получить номер оформленного заказа")
    def get_new_order_number(self):
        new_order_number_element = self.wait_and_find_element(MainPageLocators.NUMBER_NEW_ORDER)
        initial_text = new_order_number_element.text

        self.wait_for_text_change(new_order_number_element, initial_text)

        return int(new_order_number_element.text)



