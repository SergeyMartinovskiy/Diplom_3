import allure
from data import *
import urls
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeed(BasePage):
    @allure.title('Открыть окно с деталями заказа при клике на карточку заказ')
    def click_to_order_card(self):
        self.wait_and_click_element(OrderFeedLocators.ORDER_WINDOW_IN_LIST)

    @allure.title('')
    def waiting_number_of_order(self):
        self.wait_and_find_element(OrderFeedLocators.NUMBER_ORDER)



