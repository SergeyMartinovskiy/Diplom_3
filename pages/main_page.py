import time

import allure
from urls import Main_URL
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

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



    @allure.step("Получить Email для авторизации из сгенерированных данных")
    def get_user_email(self, user_response):
        email = user_response["email"]
        return email

    @allure.step("Получить Password для авторизации из сгенерированных данных")
    def get_user_password(self, user_response):
        password = user_response["password"]
        return password

    @allure.step("Кликнуть по кнопке закрытия всплывающего окна")
    def click_order_card_x_button(self):
        x_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.X_BUTTON_POP_WINDOW_ORDER)
        )
        x_button.click()

    @allure.step("Получить номер созданного заказа и закрыть окно")
    def get_order_number_and_close(self, timeout=15):
            order_number = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(MainPageLocators.NUMBER_NEW_ORDER)
            ).text.strip()
            self.click_order_card_x_button()
            return order_number


