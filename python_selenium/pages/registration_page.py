from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from utils.locators import Locators_Registration_Page
from utils import data


class Registration_Page(BasePage):

    def enter_name(self):
        self.driver.find_element(*Locators_Registration_Page.Name_XPATH).send_keys(*data.Name)

    def enter_email(self):
        self.driver.find_element(*Locators_Registration_Page.Email_XPATH).send_keys(*data.Email)

    def enter_password(self):
        self.driver.find_element(*Locators_Registration_Page.Password_XPATH).send_keys(*data.Password)

    def click_check(self):
        self.driver.find_element(*Locators_Registration_Page.Check_Button_XPATH).click()

    def click_gender(self):
        Select(self.driver.find_element(*Locators_Registration_Page.Dropdown_Gender_XPATH)).select_by_visible_text(
            "Female")

    def click_employment(self):
        self.driver.find_element(*Locators_Registration_Page.Employment_Status_XPATH).click()

    def enter_dateofbirth(self):
        self.driver.find_element(*Locators_Registration_Page.Date_of_Birth_XPATH).send_keys(*data.DateOfBirth)

    def click_submit(self):
        self.driver.find_element(*Locators_Registration_Page.Submit_Button_XPATH).click()

    def alert_message(self):
        try:
            alert_element = self.driver.find_element(*Locators_Registration_Page.Alert_Success_XPATH)
            alert_text = alert_element.text
            expected_alert = "Success!"
            if alert_text == expected_alert:
                print("Success alert found.")
            else:
                print("Alert text does not match the expected message."
                      " Expected: '{}' Actual: '{}'".format(expected_alert, alert_text))
        except NoSuchElementException:
            print("There is no such alert.")

    def click_shop(self):
        self.driver.find_element(*Locators_Registration_Page.Shop_Button_XPATH).click()
