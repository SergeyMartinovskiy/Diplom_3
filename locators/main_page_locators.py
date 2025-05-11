from selenium.webdriver.common.by import By

class MainPageLocators:
    TITLE_MAIN_PAGE = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')
    ORDERED_FEED_TITLE = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")
    ORDERED_FEED_BUTTON = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    FLUOR_BUN_BUTTON = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    DETAILS_INGREDIENT = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")
    DETAILS_INGREDIENT_FLUOR_BUN = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")






