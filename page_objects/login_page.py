from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # Locators
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")
    
    def login(self, email, password):
        self.input_text(*self.EMAIL_INPUT, email)
        self.input_text(*self.PASSWORD_INPUT, password)
        self.click_element(*self.LOGIN_BUTTON)
    
    def get_error_message(self):
        return self.find_element(*self.ERROR_MESSAGE).text