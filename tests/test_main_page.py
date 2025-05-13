import allure
from data import *
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from pages.personal_account_page import PersonalAccountPage
from locators.personal_account_page_locators import PersonalAccountPageLocators

import data

class TestMainPageFunction:
    @allure.title('Переход по клику на кнопку Конструктор')
    def test_transfer_click_to_button_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        main_page.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        assert main_page.wait_and_find_element(MainPageLocators.TITLE_MAIN_PAGE).text == 'Соберите бургер'

    @allure.title('Переход по клику на кнопку Лента заказов')
    def test_transfer_click_to_button_ordered_feed(self, driver):
        main_page = MainPage(driver)

        main_page.click_personal_account_button()
        main_page.click_element(MainPageLocators.ORDERED_FEED_BUTTON)
        assert main_page.wait_and_find_element(MainPageLocators.ORDERED_FEED_TITLE).text == 'Лента заказов'

    @allure.title('Проверка появления всплывающего окна с деталями ингредиентов при клике на ингредиент')
    def test_success_open_details_about_ingredients(self, driver):
        main_page = MainPage(driver)

        main_page.close_modal_if_open()
        main_page.wait_and_click_element(MainPageLocators.FLUOR_BUN_BUTTON)
        main_page.close_modal_if_open()
        assert main_page.wait_and_find_element(MainPageLocators.DETAILS_INGREDIENT).text == 'Детали ингредиента'

    @allure.title('Проверка возможности закрытия всплывающего окна с деталями ингредиентов при клике на ингредиент')
    def test_close_pop_up_window_ingredient_details(self, driver):
        main_page = MainPage(driver)

        main_page.close_modal_if_open()
        main_page.wait_and_click_element(MainPageLocators.FLUOR_BUN_BUTTON)
        main_page.close_modal_if_open()
        main_page.wait_and_click_element(MainPageLocators.X_BUTTON_POP_UP_WINDOW_DET_INGRED)
        assert main_page.wait_and_find_element(MainPageLocators.TITLE_MAIN_PAGE).text == 'Соберите бургер'

    @allure.title('Проверка увеличекния счетчика ингредиента при добавлении его в заказ')
    def test_increase_counter_inredient_when_add_ingredient(self, driver):
        main_page = MainPage(driver)

        main_page.close_modal_if_open()
        main_page.add_bun_to_order_busket()
        main_page.close_modal_if_open()
        assert main_page.wait_and_find_element(MainPageLocators.COUNT_FLUOR_BUN_AFTER_ADD).text == '2'

    @allure.title('Проверка возможности оформления заказа залогиненным пользователем')
    def test_success_order_login_user(self, driver):
        main_page = MainPage(driver)

        main_page.click_personal_account_button()
        personal_page = PersonalAccountPage(driver)
        personal_page.fill_field_email(data.email)
        personal_page.fill_field_password(data.password)
        personal_page.click_enter_button()
        main_page = MainPage(driver)

        main_page.close_modal_if_open()
        main_page.add_bun_to_order_busket()
        main_page.close_modal_if_open()
        main_page.wait_and_click_element(MainPageLocators.BUTTON_ORDER)
        assert main_page.wait_and_find_element(MainPageLocators.TITLE_CONFIRM_ORDER).text == 'Ваш заказ начали готовить'





