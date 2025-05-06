from selenium.webdriver.common.by import By

class RecoveryPasswordPageLocators:


    RECOVERY_PASSWORD_BUTTON = (By.XPATH, '//a[contains(text(),"Восстановить пароль")]')
    TITLE_RECOVERY_PAGE = (By.XPATH, '//h2[contains(text(),"Восстановление пароля")]')
    EMAIL_FIELD  = (By.XPATH, '//input[@name="name"]')
    RECOVERY_BUTTON = (By.XPATH, '//button[contains(text(),"Восстановить")]')
    NEW_PASSWORD_FIELD = (By.XPATH, '//input[@name="Введите новый пароль"]')


    EYE_BUTTON = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    SAVE_PASSWORD_BUTTON = (By.XPATH, '//button[contains(text(),"Сохранить")]')


