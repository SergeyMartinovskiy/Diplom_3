
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.recovery_password_page import RecoveryPasswordPage
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators
import allure

class TestRecoveryPasswordPage:
    @allure.title('Поверка перехода на страницу восстановления пароля по кнопке Восстановить пароль')
    def test_success_go_to_page_recovery_password(self, driver):
        main_page = MainPage(driver)
        main_page.open_start_window()
        main_page.click_personal_account_button()
        account_page = PersonalAccountPage(driver)
        account_page.click_recovery_password_button()
        recovery_page = RecoveryPasswordPage(driver)
        assert recovery_page.wait_and_find_element(RecoveryPasswordPageLocators.TITLE_RECOVERY_PAGE).text == 'Восстановление пароля'


