import allure
from data import *
import urls
from locators.order_feed_page_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeed(BasePage):
    @allure.title('Открыть окно с деталями заказа при клике на карточку заказ')
    def click_to_order_card(self):
        self.wait_and_click_element(OrderFeedLocators.ORDER_WINDOW_IN_LIST)

    @allure.title('Номер последнего заказа')
    def waiting_number_of_order(self):
        return  self.wait_and_find_element(OrderFeedLocators.ORDER_NUMBER_IN_HISTORY).text

    @allure.title('Номер заказа в разделе В работе на экране Лента Заказов')
    def get_number_order_in_works(self):
        number_order_in_works = self.wait_and_find_element((OrderFeedLocators.ORDER_IN_WORK_LIST))
        return int(number_order_in_works.text)


