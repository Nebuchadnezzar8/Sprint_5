from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers.locators import RegistrationLocators, LoginLocators
from helpers.data_generators import DataGenerator
from helpers.urls import Urls


class TestRegistration:

    # успешная регистрация
    def test_successful_registration(self, driver, register_page_open):
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys("ivan")
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(DataGenerator.generate_email())
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(DataGenerator.generate_password())

        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginLocators.SIGN_IN_BUTTON))

        assert driver.current_url == Urls.LOGIN_URL

    # некорректный пароль
    def test_registration_with_short_password(self, driver, register_page_open):
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys("ivan")
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(DataGenerator.generate_email())
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(DataGenerator.generate_short_password())

        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(RegistrationLocators.INVALID_PASSWORD_MESSAGE)).text

        assert error_message == "Некорректный пароль"
