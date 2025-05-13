import time

import allure
from urls import Main_URL
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException


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
        self.wait_and_click_element(MainPageLocators.X_BUTTON_POP_WINDOW_ORDER)

    @allure.step("Получить номер созданного заказа и закрыть окно")
    def get_order_number_and_close(self, timeout=15):
            order_number = (self.wait_and_find_element(MainPageLocators.NUMBER_NEW_ORDER).text.strip())
            self.click_order_card_x_button()
            return order_number

    @allure.title('Закрыть модальное окно, если оно открыто')
    def close_modal_if_open(self):
        super().close_modal_if_open(MainPageLocators.MODAL_CLOSE_BUTTON)
#************#
    @allure.title('Нажать на кнопку Конструктор')
    def click_button_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.title('Получить заголовок страницы Конструктор')
    def constructor_title(self):
        return self.wait_and_find_element(MainPageLocators.TITLE_MAIN_PAGE).text

    @allure.title('Нажать на кнопку Лента заказов')
    def click_button_order_feed(self):
        self.click_element(MainPageLocators.ORDERED_FEED_BUTTON)

    @allure.title('Получить заголовок страницы Лента заказов')
    def order_feed_title(self):
        return self.wait_and_find_element(MainPageLocators.ORDERED_FEED_TITLE).text

    @allure.title('Нажать на Флюоресцентную булочку. Вызов окна с подробностями ингредиента')
    def click_flour_bun_button(self):
        self.wait_and_click_element(MainPageLocators.FLUOR_BUN_BUTTON)

    @allure.title('Получить заголовок окна с деталями нгредиента')
    def flour_bun_detail_title(self):
        return self.wait_and_find_element(MainPageLocators.DETAILS_INGREDIENT).text

    @allure.title('Нажать кнопку Х в окне деталей ингредиента')
    def click_x_button_detail_ingredient(self):
        self.wait_and_click_element(MainPageLocators.X_BUTTON_POP_UP_WINDOW_DET_INGRED)

    @allure.title('Получение индекса добавленной ингредиента')
    def count_flour_bun_after_add_title(self):
        return self.wait_and_find_element(MainPageLocators.COUNT_FLUOR_BUN_AFTER_ADD).text