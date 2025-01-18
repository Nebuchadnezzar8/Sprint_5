from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers.locators import ConstructorLocators


class TestConstructorNavigation:

    # переходы к разделу "Булки"
    def test_buns_navigation(self, driver, user_authorization):
        tab_element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(ConstructorLocators.BUNS_TAB))
        WebDriverWait(driver, 3).until(lambda d: 'tab_tab_type_current' in tab_element.get_attribute('class'))
        class_attribute = tab_element.get_attribute('class')
        assert 'tab_tab_type_current' in class_attribute

    # переходы к разделу "Соусы"
    def test_souses_navigation(self, driver, user_authorization):
        tab_element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(ConstructorLocators.SOUSES_TAB))
        tab_element.click()
        WebDriverWait(driver, 3).until(lambda d: 'tab_tab_type_current' in tab_element.get_attribute('class'))
        class_attribute = tab_element.get_attribute('class')
        assert 'tab_tab_type_current' in class_attribute

    # переходы к разделу "Начинки"
    def test_toppings_navigation(self, driver, user_authorization):
        tab_element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(ConstructorLocators.TOPPINGS_TAB))
        tab_element.click()
        WebDriverWait(driver, 3).until(lambda d: 'tab_tab_type_current' in tab_element.get_attribute('class'))
        class_attribute = tab_element.get_attribute('class')
        assert 'tab_tab_type_current' in class_attribute
