import allure
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators
from pages.base_page import BasePage

class RecoveryPasswordPage(BasePage):
    @allure.title('Клик по кнопке Восстановить')
    def click_recovery_button(self):
        self.wait_and_find_element(RecoveryPasswordPageLocators.RECOVERY_BUTTON).click_element()

    @allure.title('Заполнение поля email')
    def fill_field_email(self, email):
        self.wait_and_find_element(RecoveryPasswordPageLocators.EMAIL_FIELD).send_keys(email)

    @allure.title('Заполнение поля пароля новым значением')
    def fill_field_new_password(self, password):
        self.wait_and_find_element(RecoveryPasswordPageLocators.NEW_PASSWORD_FIELD).send_keys(password)

    @allure.title('')
    def
