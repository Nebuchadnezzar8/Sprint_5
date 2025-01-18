import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers.locators import RegistrationLocators, LoginLocators, MainPageLocators, AuthorizationUser
from helpers.urls import Urls
from helpers.user_data import UserData


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def base_page_open(driver):
    driver.get(Urls.BASE_URL)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.ACCOUNT_LOGIN_BUTTON))


@pytest.fixture
def register_page_open(driver, base_page_open):
    driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginLocators.REGISTER_LINK)).click()


@pytest.fixture
def login_page_open(driver):
    driver.get(Urls.LOGIN_URL)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginLocators.SIGN_IN_BUTTON))


@pytest.fixture
def user_authorization(driver, login_page_open):
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(UserData.EMAIL)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(UserData.PASSWORD)
    driver.find_element(*LoginLocators.SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AuthorizationUser.PLACE_ORDER_BUTTON))
