from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from utils.locators import Shop_Page
from utils import data


class Product_Page(BasePage):

    def phone_search(self):
        products = self.driver.find_elements(*Shop_Page.Products_XPATH)
        for product in products:
            product_name = product.find_element(*Shop_Page.Products_Name_XPATH).text
            if product_name == "Samsung Note 8":
                product.find_element(*Shop_Page.Products_Buttons_XPATH).click()

    def click_checkout(self):
        self.driver.find_element(*Shop_Page.Checkout_Button_XPATH).click()

    def enter_quantity(self):
        quantity_input = self.driver.find_element(*Shop_Page.Quantity_Input_XPATH)
        quantity_input.clear()
        quantity_input.send_keys(*data.Quantity)

    def check_final_amount(self):
        try:
            amount_element = self.driver.find_element(*Shop_Page.Check_Amount_CSS)
            amount_text = amount_element.text
            expected_amount = "₹. 340000"
            if amount_text == expected_amount:
                print("Correct amount found: ₹. 340000")
            else:
                print("Incorrect amount found:", amount_text)
        except NoSuchElementException:
            print("Amount element not found")

    def click_checkout_last(self):
        self.driver.find_element(*Shop_Page.Checkout_Last_Button_CSS).click()
