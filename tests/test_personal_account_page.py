import allure

import data
from pages.main_page import MainPage
from data import *
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.personal_account_page import PersonalAccountPage

class TestPersonalAccountPage:
    @allure.title('Переход по клику на Личный кабинет')
    def test_click_button_transfer_to_personal_account(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        main_page.close_modal_if_open()
        assert main_page.wait_and_find_element(PersonalAccountPageLocators.HEADING_PERSONAL_PAGE).text == 'Вход'

    @allure.title('Выход по клику из Личного кабинета')
    def test_click_button_transfer_to_history_order(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        personal_page = PersonalAccountPage(driver)
        personal_page.fill_field_email(data.email)
        personal_page.fill_field_password(data.password)
        personal_page.click_enter_button()
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        personal_page = PersonalAccountPage(driver)
        personal_page.click_exit_button()
        assert personal_page.wait_and_find_element(PersonalAccountPageLocators.HEADING_PERSONAL_PAGE).text == 'Вход'





