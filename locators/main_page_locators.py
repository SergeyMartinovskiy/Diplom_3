from selenium.webdriver.common.by import By

class MainPageLocators:
    TITLE_MAIN_PAGE = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')
    ORDERED_FEED_BUTTON = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')



