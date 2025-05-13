import allure
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators
from pages.base_page import BasePage

class RecoveryPasswordPage(BasePage):
    @allure.title('Клик по кнопке Восстановить')
    def click_recovery_button(self):
        self.wait_and_click_element(RecoveryPasswordPageLocators.RECOVERY_BUTTON)

    @allure.title('Заполнение поля email')
    def fill_field_email(self, email):
        self.wait_and_find_element(RecoveryPasswordPageLocators.EMAIL_FIELD).send_keys(email)

    @allure.title('Заполнение поля пароля новым значением')
    def fill_field_new_password(self, password):
        self.wait_and_find_element(RecoveryPasswordPageLocators.NEW_PASSWORD_FIELD).send_keys(password)

    @allure.title('Клик по элементу в виде глаза для разблюривания пароля')
    def click_to_show_hiding_passsword(self):
        self.wait_and_find_element(RecoveryPasswordPageLocators.EYE_BUTTON).click()

    @allure.title('Получение заголовка страницы Восстановения пароля')
    def title_recovery_password_page(self):
        return self.wait_and_find_element(RecoveryPasswordPageLocators.TITLE_RECOVERY_PAGE).text

    @allure.title('Получение типа в поле пароль (элементы скрытые глазиком)')
    def get_type_in_password_field(self):
        return self.wait_and_find_element(RecoveryPasswordPageLocators.NEW_PASSWORD_FIELD).get_attribute('type')