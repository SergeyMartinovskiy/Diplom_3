from selenium.webdriver.common.by import By

class OrderFeedLocators:
    TITLE_ORDER_FEED = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")
    X_BUTTON_POP_WINDOW_ORDER = (By.XPATH, "//button[@type='button']//*[name()='svg']")
    NUMBER_ORDER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]")
    ORDERED_FEED_BUTTON = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')
    TITLE_ORDER_IN_WORK = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default mb-2')])")
    ORDER_IN_WORK_LIST = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default mb-2')])[6][1]")
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]")

    ORDER_WINDOW_IN_LIST = (By.XPATH, "(//a[contains(@class,'OrderHistory_link__1iNby')])[2]")
    COMPOSITION_BURGER = (By.XPATH, '//p[contains(@class, "text_type_main-medium") and contains(@class, "mb-8")][1]')

    ORDER_HISTORY_IN_lIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list__OLh59']")