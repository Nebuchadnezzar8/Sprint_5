from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers.locators import MainPageLocators, LoginLocators, AuthorizationUser, RegistrationLocators, PasswordRecoveryLocators
from helpers.user_data import UserData


class TestUserAuthentication:

    # авторизация по кнопке «Войти в аккаунт»
    def test_login_authentication_main_page(self, driver, base_page_open):
        driver.find_element(*MainPageLocators.ACCOUNT_LOGIN_BUTTON).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(UserData.EMAIL)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(UserData.PASSWORD)
        driver.find_element(*LoginLocators.SIGN_IN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AuthorizationUser.PLACE_ORDER_BUTTON))

    # авторизация через кнопку «Личный кабинет»
    def test_login_authentication_personal_cabinet(self, driver, base_page_open):
        driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(UserData.EMAIL)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(UserData.PASSWORD)
        driver.find_element(*LoginLocators.SIGN_IN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AuthorizationUser.PLACE_ORDER_BUTTON))

    # авторизация через кнопку в форме регистрации
    def test_login_authentication_registration_form(self, driver, register_page_open):
        driver.find_element(*RegistrationLocators.LOGIN_LINK).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(UserData.EMAIL)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(UserData.PASSWORD)
        driver.find_element(*LoginLocators.SIGN_IN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AuthorizationUser.PLACE_ORDER_BUTTON))

    # авторизация через кнопку в форме восстановления пароля
    def test_login_authentication_password_recovery(self, driver, login_page_open):
        driver.find_element(*LoginLocators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*PasswordRecoveryLocators.LOGIN_LINK).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(UserData.EMAIL)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(UserData.PASSWORD)
        driver.find_element(*LoginLocators.SIGN_IN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AuthorizationUser.PLACE_ORDER_BUTTON))
