import allure

import data
from pages.main_page import MainPage
from data import *
from locators.personal_account_page_locators import PersonalAccountPageLocators
from locators.order_feed_locators import OrderFeedLocators
from pages.order_feed import OrderFeed
from pages.personal_account_page import PersonalAccountPage
from locators.main_page_locators import MainPageLocators


class TestOrderFeed:

    @allure.title('Проверка всплывающего окна с деталями при клике на заказ')
    def test_open_details_about_order(self,driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.wait_and_click_element(MainPageLocators.ORDERED_FEED_BUTTON)
        order_feed_page = OrderFeed(driver)
        order_feed_page.click_to_order_card()
        order_feed_page.close_modal_if_open()
        assert order_feed_page.wait_and_find_element(OrderFeedLocators.COMPOSITION_BURGER).text == 'Cостав'

    @allure.title('Проверка отображения заказа на странице Лента заказов')
    def test_appearance_order_in_list_order(self,driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        personal_page = PersonalAccountPage(driver)
        personal_page.fill_field_email(data.email)
        personal_page.fill_field_password(data.password)
        personal_page.click_enter_button()
        main_page.add_bun_to_order_busket()
        main_page.close_modal_if_open()
        main_page.wait_and_click_element(MainPageLocators.BUTTON_ORDER)
        order_feed = OrderFeed(driver)
        order_feed.wait_and_click_element(OrderFeedLocators.X_BUTTON_POP_WINDOW_ORDER)
        main_page.wait_and_click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        main_page.wait_and_click_element(MainPageLocators.ORDER_HISTORY_BUTTON)
        order_number = personal_page.wait_and_find_element(PersonalAccountPageLocators.ORDER_NUMBER_IN_HISTORY).text()
        main_page.wait_and_click_element(MainPageLocators.ORDERED_FEED_BUTTON)
        order_number_in_list = order_feed.wait_and_find_element(OrderFeedLocators.ORDER_HISTORY_IN_lIST).text()
        assert order_number == order_number_in_list


    @allure.title('Проверка появления номера оформленного заказа в разделе ')
    def test_check_number_order_in_field_in_work(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        personal_page = PersonalAccountPage(driver)
        personal_page.fill_field_email(data.email)
        personal_page.fill_field_password(data.password)
        personal_page.click_enter_button()

        main_page.close_modal_if_open()
        main_page.add_bun_to_order_busket()
        main_page.close_modal_if_open()
        main_page.wait_and_click_element(MainPageLocators.BUTTON_ORDER)
        order_feed = OrderFeed(driver)
        order_feed.wait_and_click_element(OrderFeedLocators.X_BUTTON_POP_WINDOW_ORDER)

        main_page.close_modal_if_open()
        main_page.click_personal_account_button()
        main_page.wait_and_click_element(MainPageLocators.ORDER_HISTORY_BUTTON)

        number_in_history = personal_page.wait_and_find_element(PersonalAccountPageLocators.ORDER_NUMBER_IN_HISTORY).text()

        main_page.wait_and_click_element(MainPageLocators.ORDER_HISTORY_BUTTON)
        order_number = order_feed.waiting_number_of_order

        assert number_in_history == order_number

