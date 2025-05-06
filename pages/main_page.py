import allure
from urls import Main_URL
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.title('Открыть стартовую страницу Стелла Бургер')
    def open_start_window(self):
        self.open_new_page(Main_URL)

    @allure.title('Нажать на кнопку Личный кабинет в шапке страницы')
    def click_personal_account_button(self):
        self.wait_and_find_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click_element()

