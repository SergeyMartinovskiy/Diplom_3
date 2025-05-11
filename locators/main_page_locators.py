from selenium.webdriver.common.by import By

class MainPageLocators:
    TITLE_MAIN_PAGE = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')
    ORDERED_FEED_TITLE = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")
    ORDERED_FEED_BUTTON = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    FLUOR_BUN_BUTTON = (By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")
    DETAILS_INGREDIENT = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")
    DETAILS_INGREDIENT_FLUOR_BUN = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    X_BUTTON_POP_UP_WINDOW_DET_INGRED = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]")

    ORDER_BUSKET =(By.XPATH, './/ul[contains(@class, "BurgerConstructor_basket__list__l9dp_")]')
    COUNT_FLUOR_BUN_AFTER_ADD = (By.XPATH, "//p[normalize-space()='2']")
    BUTTON_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    TITLE_CONFIRM_ORDER = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")

    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(),'История заказов')]")
    NUMBER_ORDER_IN_HISTORY = (By.XPATH, "//p[@class = text text_type_digits-default")



