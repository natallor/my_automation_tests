from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from utils import data
from utils.locators import Locators_Confirmation_Page


class Confirmation_Page(BasePage):

    def enter_location(self):
        self.wait_for_element_visibility(Locators_Confirmation_Page.Location_Input_XPATH).send_keys(data.Location)

    def click_dropdown(self):
        self.wait_for_element_clickable(Locators_Confirmation_Page.Dropdown_Location_XPATH).click()

    def click_checkbox(self):
        self.driver.find_element(*Locators_Confirmation_Page.Checkbox_XPATH).click()

    def click_purchase(self):
        self.driver.find_element(*Locators_Confirmation_Page.Submit_Purchase_XPATH).click()

    def check_message(self):
        try:
            alert_success = self.driver.find_element(*Locators_Confirmation_Page.Alert_Success_Text_CSS)
            alert_text = alert_success.text
            expected_alert = "Success!"
            if alert_text == expected_alert:
                print("Valid alert found: Success!")
            else:
                print("Invalid alert found. Expected: '{}' Actual: '{}'".format(expected_alert, alert_text))
        except NoSuchElementException:
            print("No alert found.")
