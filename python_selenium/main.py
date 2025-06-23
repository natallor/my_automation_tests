import unittest
from tests_cases.test_Product_Page import Test_Product_Page_And_Confirmation
from tests_cases.test_Registration_Page import Test_Registration_Page

if __name__ == "__main__":

    loader = unittest.TestLoader()
    product_tests_and_confirmation = loader.loadTestsFromTestCase(Test_Product_Page_And_Confirmation)
    registration_tests = loader.loadTestsFromTestCase(Test_Registration_Page)

    suite = unittest.TestSuite([registration_tests, product_tests_and_confirmation])

    unittest.TextTestRunner(verbosity=2).run(suite)
