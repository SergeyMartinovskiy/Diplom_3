from selenium.webdriver.common.by import By

class Locator:
    # Регистрация
    # Поле Имя
    name_field = (By.XPATH, "(//input[@name='name'])[1]")
    # Поле Email
    email_field = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    # Поле Пароль
    password_field = (By.XPATH, ".//input[@name='Пароль']")
    # Кнопка Зарегистрироваться (после ввода данных в поля Имя, почта, пароль)
    button_registration = (By.XPATH, '//button[text() = "Зарегистрироваться"]')
    # Активная надпись Зарегистрироваться (Новый пользователь)
    sign_registration = (By.XPATH, './/a[contains(text(),"Зарегистрироваться")]')

    # Кнопка "Личный кабинет"
    button_personal_account = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')
    # Кнопка "Войти в аккаунт"
    button_enter_to_account = (By.XPATH, './/button[contains(text(),"Войти в аккаунт")]')
    # Кнопка Войти
    button_enter = (By.XPATH, './/button[contains(text(),"Войти")]')
    # Активная надпись Войти на странице восстановления пароля
    button_enter_in_recovery_page = (By.XPATH, './/a[contains(text(),"Войти")]')
    #Кнопка раздела История заказов (Лента заказов)
    button_order_history = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')

    # Активная надпись Восстановить пароль
    sign_recovery_password = (By.XPATH, './/a[contains(text(),"Восстановить пароль")]')
    # Кнопка Восставноить пароль после ввода пароля
    button_recovery_password = (By.XPATH, './/button[contains(text(),"Восстановить")]')
    # Кнопка перехода Конструктор
    button_constructor = (By.XPATH, './/p[contains(text(),"Конструктор")]')
    # Кнопка Логотип Stellar Burgers
    logo_stella_burgers = (By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]//a//*[name()="svg"]')
    # Кнопка перехода - Булки
    button_bread = (By.XPATH, './/span[contains(text(),"Булки")]')
    # Кнопка перехода - Соусы
    button_sauce = (By.XPATH, './/span[contains(text(),"Соусы")]')
    # Кнопка перехода - Начинки
    button_topping = (By.XPATH, './/span[contains(text(),"Начинки")]')
    # Кнопка Выхода из аккаунта
    button_exit_from_account = (By.XPATH, './/button[contains(text(),"Выход")]')
    # Ошибка при вводе неверного пароля
    text_invalid_password = (By.XPATH, './/p[@class="input__error text_type_main-default"]')
    # Проверка текста Вход (Проверка выхода из аккаунта)
    text_enter_in_account = (By.XPATH, './/h2[contains(text(),"Вход")]')
    # Проверка перехода в личный кабинет через текст "Профиль" на странице Личного кабинета
    text_in_personal_account = (By.XPATH, './/p[@class="Account_text__fZAIn text text_type_main-default"]')
    # Проверка перехода по кнопке Конструктор текстом "Соберите бургер"
    text_in_page_constructor = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')
    # Проверка перехода по кнопке Логотипа - текстом "Оформить заказ"
    text_in_main_page = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')
    # Выбранная секция в конструкторе
    choose_section_of_item = (By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")
    # Текст Соус на странице выбора вариантов Соуса (Конструктор)
    text_sauce_in_scroll = (By.XPATH, './/h2[contains(text(),"Соусы")]')
    # Текст Начинки на странице выбора вариантов начинок (Конструктор)
    text_topping_in_scroll = (By.XPATH, './/h2[contains(text(),"Начинки")]')
    # Текст Булки на странице выбора вариантов Булок (Конструктор)
    text_bread_in_scroll = (By.XPATH, './/h2[contains(text(),"Булки")]')
    # Кнопка пересохранения пароля

