import allure
from data import *
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators




class TestMainPageFunction:
    @allure.title('Переход по клику на кнопку Конструктор')
    def test_transfer_click_to_button_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        main_page.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        assert main_page.wait_and_find_element(MainPageLocators.TITLE_MAIN_PAGE).text == 'Соберите бургер'

    @allure.title('Переход по клику на кнопку Лента заказов')
    def test_transfer_click_to_button_ordered_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        main_page.click_element(MainPageLocators.ORDERED_FEED_BUTTON)
        assert main_page.wait_and_find_element(MainPageLocators.ORDERED_FEED_TITLE).text == 'Лента заказов'

    @allure.title('Проверка появления всплывающего окна с деталями ингредиентов при клике на ингредиент')
    def test_success_open_details_about_ingredients(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.close_modal_if_open()
        main_page.wait_and_click_element(MainPageLocators.FLUOR_BUN_BUTTON)
        main_page.close_modal_if_open()
        assert main_page.wait_and_find_element(MainPageLocators.DETAILS_INGREDIENT).text == 'Детали ингредиента'


