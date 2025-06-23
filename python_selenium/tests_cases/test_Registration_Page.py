import unittest
from selenium import webdriver
from pages.registration_page import Registration_Page
from utils.data import Registration


class Test_Registration_Page(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Registration)
        self.driver.maximize_window()


    def test_registration_data(self):
        data_input = Registration_Page(self.driver)
        data_input.enter_name()
        data_input.enter_email()
        data_input.enter_password()
        data_input.click_check()
        data_input.click_gender()
        data_input.click_employment()
        data_input.enter_dateofbirth()
        data_input.click_submit()
        data_input.alert_message()
        data_input.click_shop()


    def tearDown(self):
        self.driver.quit()


    if __name__ == '__main__':
        unittest.main()
