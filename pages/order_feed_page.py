import allure
from data import *
import urls
from locators.order_feed_page_locators import OrderFeedLocators
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

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

    @allure.step('Скроллим до необходимого элемента')
    def scrolling_to_block_of_elements(self, locator):
        element = self.wait_and_find_element(locator)
        self.scroll_to_element(element)

    def scroll_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    @allure.step("Получить номер последнего заказа")
    def get_order_number(self):
        element = self.wait_and_find_element(OrderFeedLocators.ORDER_NUMBER_IN_HISTORY)
        return element.text

    @allure.step("Получить значение счётчика всех заказов на странице 'Лента заказов'")
    def get_orders_counter(self):
        number = self.wait_and_find_element(OrderFeedLocators.ORDER_COUNTER)
        return int(number.text)

    @allure.step("Получить значение счётчика 'Выполнено за сегодня' заказав на странице 'Лента заказов'")
    def get_orders_counter_today(self):
        number = self.wait_and_find_element(OrderFeedLocators.ORDER_COUNTER_TODAY)
        return int(number.text)




