import data
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.recovery_password_page import RecoveryPasswordPage
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators
import allure

class TestRecoveryPasswordPage:
    @allure.title('Поверка перехода на страницу восстановления пароля '
                  'по кнопке Восстановить пароль')
    def test_success_go_to_page_recovery_password(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        account_page = PersonalAccountPage(driver)
        account_page.click_recovery_password_button()
        recovery_page = RecoveryPasswordPage(driver)
        assert recovery_page.wait_and_find_element(RecoveryPasswordPageLocators.TITLE_RECOVERY_PAGE).text == 'Восстановление пароля'

    @allure.title('Проверка перехода на страницу Восстановления пароля - '
                  'ввод почты и клик по кнопке Восстановить')
    def test_transfer_enter_email_and_click_recovery_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        account_page = PersonalAccountPage(driver)
        account_page.click_recovery_password_button()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.fill_field_email(data.email)
        recovery_page.click_recovery_button()
        assert recovery_page.wait_and_find_element(RecoveryPasswordPageLocators.TITLE_RECOVERY_PAGE).text == 'Восстановление пароля'

    @allure.title('Проверка клика по кнопке Глаз, делает поле пароля '
                  'скрытым/открытым на странице Восстановления пароля')
    def test_click_eye_button_to_open_password(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        account_page = PersonalAccountPage(driver)
        account_page.click_recovery_password_button()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.fill_field_email(data.email)
        recovery_page.click_recovery_button()
        recovery_page.fill_field_new_password(data.new_password)
        assert recovery_page.wait_and_find_element(RecoveryPasswordPageLocators.
                                                   NEW_PASSWORD_FIELD).get_attribute('type') == 'password'
        recovery_page.close_modal_if_open()
        recovery_page.click_to_show_hiding_passsword()
        assert recovery_page.wait_and_find_element(RecoveryPasswordPageLocators.
                                                   NEW_PASSWORD_FIELD).get_attribute('type') == 'text'
