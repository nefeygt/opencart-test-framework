from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CheckoutPage(BasePage):
    # Locators
    FIRST_NAME = (By.ID, "input-payment-firstname")
    LAST_NAME = (By.ID, "input-payment-lastname")
    EMAIL = (By.ID, "input-payment-email")
    TELEPHONE = (By.ID, "input-payment-telephone")
    ADDRESS_1 = (By.ID, "input-payment-address-1")
    CITY = (By.ID, "input-payment-city")
    POSTCODE = (By.ID, "input-payment-postcode")
    COUNTRY = (By.ID, "input-payment-country")
    REGION = (By.ID, "input-payment-zone")
    TERMS_CHECKBOX = (By.CSS_SELECTOR, "input[name='agree']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[value='Continue']")
    CONFIRM_ORDER_BUTTON = (By.ID, "button-confirm")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content h1")

    def fill_billing_details(self, test_data=None):
        if test_data is None:
            test_data = {
                "firstname": "John",
                "lastname": "Doe",
                "email": "john.doe@example.com",
                "telephone": "1234567890",
                "address_1": "123 Test Street",
                "city": "Test City",
                "postcode": "12345",
                "country": "Finland",
                "region": "Uusimaa"
            }

        # Fill in personal details
        self.input_text(*self.FIRST_NAME, test_data["firstname"])
        self.input_text(*self.LAST_NAME, test_data["lastname"])
        self.input_text(*self.EMAIL, test_data["email"])
        self.input_text(*self.TELEPHONE, test_data["telephone"])
        
        # Fill in address
        self.input_text(*self.ADDRESS_1, test_data["address_1"])
        self.input_text(*self.CITY, test_data["city"])
        self.input_text(*self.POSTCODE, test_data["postcode"])
        
        # Select country and region
        country_select = Select(self.find_element(*self.COUNTRY))
        country_select.select_by_visible_text(test_data["country"])
        
        # Wait for region options to load
        self.wait.until(lambda d: Select(self.find_element(*self.REGION)).options)
        region_select = Select(self.find_element(*self.REGION))
        region_select.select_by_visible_text(test_data["region"])
        
        # Accept terms
        self.click_element(*self.TERMS_CHECKBOX)
        
        # Continue to next step
        self.click_element(*self.CONTINUE_BUTTON)

    def confirm_order(self):
        self.click_element(*self.CONFIRM_ORDER_BUTTON)

    def get_success_message(self):
        return self.find_element(*self.SUCCESS_MESSAGE).text