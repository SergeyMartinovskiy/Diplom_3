import allure
from data import *
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators




class TestMainPageFunction:
    @allure.title('')
    def test_transfer_click_to_button_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        main_page.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        assert main_page.wait_and_find_element(MainPageLocators.TITLE_MAIN_PAGE).text == 'Соберите бургер'


