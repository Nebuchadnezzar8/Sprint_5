from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers.locators import AuthorizationUser, LoginLocators
from helpers.urls import Urls


class TestUserNavigation:

    # переход по клику на «Личный кабинет»
    def test_navigation_personal_cabinet(self, driver, user_authorization):
        driver.find_element(*AuthorizationUser.PERSONAL_CABINET_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AuthorizationUser.PROFILE_BUTTON))
        assert driver.current_url == Urls.PERSONAL_CABINET_URL

    #  переход по клику на лого
    def test_navigation_logo(self, driver, user_authorization):
        driver.find_element(*AuthorizationUser.PERSONAL_CABINET_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AuthorizationUser.PROFILE_BUTTON))
        driver.find_element(*AuthorizationUser.LOGO_LINK).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AuthorizationUser.PLACE_ORDER_BUTTON))

    #  переход по клику на конструктор
    def test_navigation_constructor(self, driver, user_authorization):
        driver.find_element(*AuthorizationUser.PERSONAL_CABINET_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AuthorizationUser.PROFILE_BUTTON))
        driver.find_element(*AuthorizationUser.CONSTRUCTOR_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AuthorizationUser.PLACE_ORDER_BUTTON))

    #  выход по кнопке «Выйти» в личном кабинете
    def test_navigation_log_out(self, driver, user_authorization):
        driver.find_element(*AuthorizationUser.PERSONAL_CABINET_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AuthorizationUser.PROFILE_BUTTON))
        driver.find_element(*AuthorizationUser.LOG_OUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginLocators.SIGN_IN_BUTTON))
        assert driver.current_url == Urls.LOGIN_URL
