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




    @allure.title('Проверка появления номера оформленного заказа в разделе В работе')
    def test_check_number_order_in_field_inwork(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        personal_page = PersonalAccountPage(driver)
        personal_page.fill_field_email(data.email)
        personal_page.fill_field_password(data.password)
        personal_page.click_enter_button()
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.close_modal_if_open()
        main_page.add_bun_to_order_busket()
        main_page.close_modal_if_open()
        main_page.wait_and_click_element(MainPageLocators.BUTTON_ORDER)
        number_order_in_window = main_page.get_new_order_number()
        main_page.wait_and_click_element(OrderFeedLocators.X_BUTTON_POP_WINDOW_ORDER)
        main_page.wait_and_click_element(MainPageLocators.ORDERED_FEED_BUTTON)
        order_feed = OrderFeed(driver)

        order_number_in_work_list = order_feed.wait_and_find_element(OrderFeedLocators.TITLE_ORDER_IN_WORK).text
        assert number_order_in_window == order_number_in_work_list

