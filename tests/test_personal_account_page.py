import allure
from pages.main_page import MainPage
from data import *
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.personal_account_page import PersonalAccountPage

class TestPersonalAccountPage:
    @allure.title('Переход по клику Личный кабинет')
    def test_click_button_transfer_to_personal_account(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        main_page.close_modal_if_open()
        assert main_page.wait_and_find_element(PersonalAccountPageLocators.HEADING_PERSONAL_PAGE).text == 'Вход'

    @allure.title('Переход по клику в раздел Истории заказов из Личного кабинета')
    def test_click_button_transfer_to_history_order(self, driver):

