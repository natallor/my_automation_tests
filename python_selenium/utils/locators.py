from selenium.webdriver.common.by import By


class Locators_Registration_Page:
    Name_XPATH = (By.XPATH, "//div[@class='form-group']//input[@name='name']")
    Email_XPATH = (By.XPATH, "//input[@name='email']")
    Password_XPATH = (By.XPATH, "//input[@id='exampleInputPassword1']")
    Check_Button_XPATH = (By.XPATH, "//input[@id='exampleCheck1']")
    Dropdown_Gender_XPATH = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    Employment_Status_XPATH = (By.XPATH, "//input[@id='inlineRadio2']")
    Date_of_Birth_XPATH = (By.XPATH, "//input[@name='bday']")
    Submit_Button_XPATH = (By.XPATH, "//input[@value='Submit']")
    Alert_Success_XPATH = (By.XPATH, "//strong[normalize-space()='Success!']")
    Shop_Button_XPATH = (By.XPATH, "//a[normalize-space()='Shop']")


class Shop_Page:
    Products_XPATH = (By.XPATH, "//div[@class='card h-100']")
    Products_Name_XPATH = (By.XPATH, "div/h4/a")
    Products_Buttons_XPATH = (By.XPATH, "div/button")
    Checkout_Button_XPATH = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    Quantity_Input_XPATH = (By.XPATH, "//input[@id='exampleInputEmail1']")
    Check_Amount_CSS = (By.CSS_SELECTOR, "td[class='text-right'] h3 strong")
    Checkout_Last_Button_CSS = (By.CSS_SELECTOR, "button[class='btn btn-success']")


class Locators_Confirmation_Page:
    Location_Input_XPATH = (By.XPATH, "//input[@id='country']")
    Dropdown_Location_XPATH = (By.XPATH, "//a[normalize-space()='Poland']")
    Checkbox_XPATH = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    Submit_Purchase_XPATH = (By.XPATH, "//input[@value='Purchase']")
    Alert_Success_Text_CSS = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible'] strong")
