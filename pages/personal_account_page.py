import allure
from data import *
from pages.base_page import BasePage
from urls import *
from locators.personal_account_page_locators import PersonalAccountPageLocators

class PersonalAccountPage(BasePage):

    @allure.title('Заполнение поля email')
    def fill_field_email(self, email):
        self.wait_and_find_element(PersonalAccountPageLocators.EMAIL_FIELD).send_keys(email)

    @allure.title('Заполнение поля Пароль')
    def fill_field_password(self, password):
        self.wait_and_find_element(PersonalAccountPageLocators.PASSWORD_FIELD).send_keys(password)

    @allure.title('Авторизция нажатием кнопки Войти')
    def click_enter_button(self):
        self.wait_and_find_element(PersonalAccountPageLocators.ENTER_BUTTON).click()

    @allure.title('Клик по надписи Профиль в личном кабинете')
    def click_profile_button(self):
        self.wait_and_find_element(PersonalAccountPageLocators.PROFILE_BUTTON).click()

    @allure.title('Клик по надписи История заказов в личном кабинете')
    def click_order_history_button(self):
        self.wait_and_find_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON).click()

    @allure.title('Клик по кнопке Выход в личном кабинете')
    def click_exit_button(self):
        self.wait_and_find_element(PersonalAccountPageLocators.EXIT_BUTTON).click()

    @allure.title('Получение номера последнего заказа')
    def get_last_number_order(self):
        self.wait_and_find_element(PersonalAccountPageLocators.LAST_ORDER_NUMBER_IN_HISTORY).text()

    @allure.title('Клик по кнопке Восстановить пароль')
    def click_recovery_password_button(self):
        self.wait_and_find_element(PersonalAccountPageLocators.RECOVERY_PASSWORD_BUTTON).click()

    @allure.step("Получить номер последнего заказа")
    def get_order_number(self):
        element = self.wait_and_find_element(PersonalAccountPageLocators.ORDER_NUMBER_IN_HISTORY)
        return element.text

    @allure.title('Заполнение поля email для регистрации')
    def fill_field_reg_email(self, email):
        self.wait_and_find_element(PersonalAccountPageLocators.REGISTRATION_EMAIL).send_keys(email)

    @allure.title('Заполнение поля Пароль для регистрации')
    def fill_field_reg_password(self, password):
        self.wait_and_find_element(PersonalAccountPageLocators.REGISTRATION_PASSWORD).send_keys(password)

    @allure.title('Заполнение поля имя для регистрации')
    def fill_field_reg_name(self, name):
        self.wait_and_find_element(PersonalAccountPageLocators.REGISTRATION_NAME).send_keys(name)

    @allure.title('Получение заголовка Личного кабинета (Вход)')
    def title_enter_personal_account(self):
        return self.wait_and_find_element(PersonalAccountPageLocators.HEADING_PERSONAL_PAGE).text

    @allure.title('Получение заголовка в Личном кабиете')
    def title_in_personal_account(self):
        return self.wait_and_find_element(PersonalAccountPageLocators.TEXT_IN_PERSONAL_ACCOUNT).text

    #@allure.title('')