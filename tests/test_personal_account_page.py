import allure

import data
from pages.main_page import MainPage
from data import *
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.personal_account_page import PersonalAccountPage

# Тесты по переходу по клику на Личный кабинет выполнил в двух вариантах.
# Просто по нажатию на кнопку и полноценный переход в личный кабинет пользователя

class TestPersonalAccountPage:
    @allure.title('Переход по клику на Личный кабинет')
    def test_click_button_transfer_to_personal_account(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        main_page.close_modal_if_open()
        assert main_page.wait_and_find_element(PersonalAccountPageLocators.HEADING_PERSONAL_PAGE).text == 'Вход'

    @allure.title('Переход в Личный кабинет пользователя')
    def test_click_button_transfer_to_personal_account(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        personal_page = PersonalAccountPage(driver)
        personal_page.fill_field_email(data.email)
        personal_page.fill_field_password(data.password)
        personal_page.click_enter_button()
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        assert main_page.wait_and_find_element(PersonalAccountPageLocators.
                                               TEXT_IN_PERSONAL_ACCOUNT).text == 'В этом разделе вы можете изменить свои персональные данные'

    @allure.title('Выход по клику из Личного кабинета')
    def test_click_exit_button_from_personal_account(self, driver):
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

    @allure.title('Проверка перехода в раздел История заказов')
    def test_click_transfer_history_order_in_personal_account(self, driver):
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
        personal_page.close_modal_if_open()
        personal_page.click_order_history_button()
        expect_url = 'https://stellarburgers.nomoreparties.site/account/order-history'
        assert personal_page.compare_urls(expect_url)






