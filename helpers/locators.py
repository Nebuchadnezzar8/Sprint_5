from selenium.webdriver.common.by import By


# локаторы на форме регистрации
class RegistrationLocators:
    NAME_INPUT = (By.XPATH, "//input[@name='name']")  # поле "Имя"
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")  # поле "Email"
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # поле "Пароль"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    INVALID_PASSWORD_MESSAGE = (
    By.XPATH, "//p[text()='Некорректный пароль']")  # валидация с текстом "Некорректный пароль"
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']") # ссылка на страницу входа


# локаторы на форме авторизации
class LoginLocators:
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[1]")  # поле "Email"
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # поле "Пароль"
    SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти"
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")  # ссылка "Зарегистрироваться"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # ссылка на восстановление пароля


# локаторы для главной страницы
class MainPageLocators:
    ACCOUNT_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    PERSONAL_CABINET_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")  # войти в личный кабинет


# локаторы для авторизованного пользователя
class AuthorizationUser:
    PERSONAL_CABINET_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")  # войти в личный кабинет
    PROFILE_BUTTON = (By.XPATH, "//a[@href='/account/profile']")  # Кнопка "Профиль"
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка "Оформить заказ"
    LOGO_LINK = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # логотип
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # конструктор
    LOG_OUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # кнопка "Выход" из профиля


# локаторы для формы восстановления пароля
class PasswordRecoveryLocators:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # ссылка "Войти"


# локаторы для разделов в конструкторе
class ConstructorLocators:
    BUNS_TAB = (By.XPATH, "//div[span[text()='Булки']]")  # таб "Булки"
    SOUSES_TAB = (By.XPATH, "//div[span[text()='Соусы']]")  # таб "Соусы"
    TOPPINGS_TAB = (By.XPATH, "//div[span[text()='Начинки']]")  # таб "Начинки"
