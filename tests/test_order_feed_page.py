import allure

import data
from pages.main_page import MainPage
from data import *
from locators.personal_account_page_locators import PersonalAccountPageLocators
from locators.order_feed_page_locators import OrderFeedLocators
from pages.order_feed_page import OrderFeed
from pages.personal_account_page import PersonalAccountPage
from locators.main_page_locators import MainPageLocators


class TestOrderFeed:

    @allure.title('Проверка всплывающего окна с деталями при клике на заказ')
    def test_open_details_about_order(self,driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeed(driver)
        main_page.click_button_order_feed()
        order_feed_page.click_to_order_card()
        main_page.close_modal_if_open()
        assert order_feed_page.title_detail_order() == 'Cостав'

    @allure.title('Проверка отображения заказа пользователя из раздела История заказов'
                  'отображаются на странице Лента заказов.')
    def test_appearance_order_in_list_order(self,driver):
        main_page = MainPage(driver)
        personal_page = PersonalAccountPage(driver)
        order_feed = OrderFeed(driver)
        main_page.click_personal_account_button()
        personal_page.click_registration_button()
        main_page.close_modal_if_open()
        reg_name = data.gen_name()
        reg_email = data.gen_email()
        reg_password = data.gen_password()
        personal_page.fill_field_reg_name(reg_name)
        personal_page.fill_field_reg_email(reg_email)
        personal_page.fill_field_reg_password(reg_password)
        personal_page.click_reg_button_in_reg_new_account()
        main_page.close_modal_if_open()
        personal_page.fill_field_email(reg_email)
        personal_page.fill_field_password(reg_password)
        personal_page.click_enter_button()
        main_page.add_bun_to_order_busket()
        main_page.close_modal_if_open()
        main_page.click_button_order()
        main_page.close_modal_if_open()
        main_page.get_order_number_and_close()
        main_page.close_modal_if_open()
        main_page.click_personal_account_button()
        main_page.click_order_history_button()
        history_number = personal_page.get_order_number()
        main_page.close_modal_if_open()
        main_page.click_button_order_feed()
        main_page.close_modal_if_open()
        order_number_in_list = str(order_feed.get_order_number())
        assert history_number == order_number_in_list

    @allure.title('Проверка появления номера оформленного заказа в Работе')
    def test_check_number_order_in_field_in_work(self, driver):
        main_page = MainPage(driver)
        personal_page = PersonalAccountPage(driver)
        order_feed = OrderFeed(driver)
        main_page.click_personal_account_button()
        personal_page.fill_field_email(data.email)
        personal_page.fill_field_password(data.password)
        personal_page.click_enter_button()
        main_page.add_bun_to_order_busket()
        main_page.close_modal_if_open()
        main_page.click_button_order()
        main_page.close_modal_if_open()
        order_number = main_page.get_order_number_and_close()
        main_page.close_modal_if_open()
        main_page.click_button_order_feed()
        number_order_in_work = str(order_feed.get_number_order_in_works())
        assert order_number == number_order_in_work


    @allure.title('Проверка увеличения счетчика Выполнено за все время '
                  ' при выполнении нового заказа')
    def test_increase_count_alltime_orders_when_make_order(self, driver):
        main_page = MainPage(driver)
        personal_page = PersonalAccountPage(driver)
        order_feed = OrderFeed(driver)
        main_page.click_personal_account_button()
        personal_page.fill_field_email(data.email)
        personal_page.fill_field_password(data.password)
        personal_page.click_enter_button()
        main_page.click_button_order_feed()
        main_page.close_modal_if_open()
        count_before_order = order_feed.get_orders_counter()
        main_page.click_button_constructor()
        main_page.close_modal_if_open()
        main_page.add_bun_to_order_busket()
        main_page.close_modal_if_open()
        main_page.click_button_order()
        main_page.close_modal_if_open()
        main_page.get_order_number_and_close()
        main_page.close_modal_if_open()
        main_page.click_button_order_feed()
        count_after_order = order_feed.get_orders_counter()
        assert (count_after_order - count_before_order) == 1


    @allure.title('Проверка увеличения счетчика Выполнено за сегодня '
                  ' при выполнении нового заказа')
    def test_increase_count_today_orders_when_make_order(self, driver):
        main_page = MainPage(driver)
        personal_page = PersonalAccountPage(driver)
        order_feed = OrderFeed(driver)
        main_page.click_personal_account_button()
        personal_page.fill_field_email(data.email)
        personal_page.fill_field_password(data.password)
        personal_page.click_enter_button()
        main_page.click_button_order_feed()
        main_page.close_modal_if_open()
        count_before_order = order_feed.get_orders_counter_today()
        main_page.click_button_constructor()
        main_page.close_modal_if_open()
        main_page.add_bun_to_order_busket()
        main_page.close_modal_if_open()
        main_page.click_button_order()
        main_page.close_modal_if_open()
        main_page.get_order_number_and_close()
        main_page.close_modal_if_open()
        main_page.click_button_order_feed()
        count_after_order = order_feed.get_orders_counter_today()
        assert (count_after_order - count_before_order) == 1

