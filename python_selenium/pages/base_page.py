from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_for_element_visibility(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
