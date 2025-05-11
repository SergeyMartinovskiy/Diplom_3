from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    HEADING_PERSONAL_PAGE = (By.XPATH, "//h2[contains(text(),'Вход')]")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    ENTER_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    TEXT_IN_PERSONAL_ACCOUNT = (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']")
    PROFILE_BUTTON = (By.XPATH, "//a[contains(text(),'Профиль')]")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(),'История заказов')]")
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    HEADING_MAIN_PAGE = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, '//a[contains(text(),"Восстановить пароль")]')
    LAST_ORDER_NUMBER_IN_HISTORY = (By.XPATH, "//p[@class='text text_type_digits-default']")
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]")



