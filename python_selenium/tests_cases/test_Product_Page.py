import unittest
from selenium import webdriver
from pages.confirmation_page import Confirmation_Page
from pages.product_page import Product_Page
from utils.data import Shop


class Test_Product_Page_And_Confirmation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Shop)
        self.driver.maximize_window()


    def test_product_addition(self):
        add_product = Product_Page(self.driver)
        add_product.phone_search()
        add_product.click_checkout()
        add_product.enter_quantity()
        add_product.check_final_amount()
        add_product.click_checkout_last()


    def test_confirmation(self):
        self.test_product_addition()
        confirmation_with_product = Confirmation_Page(self.driver)
        confirmation_with_product.enter_location()
        confirmation_with_product.click_dropdown()
        confirmation_with_product.click_checkbox()
        confirmation_with_product.click_purchase()
        confirmation_with_product.check_message()


    def tearDown(self):
        self.driver.quit()


    if __name__ == '__main__':
        unittest.main()