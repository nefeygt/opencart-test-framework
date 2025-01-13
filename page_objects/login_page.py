from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    # Updated locators
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert")  # Updated selector
    
    def login(self, email, password):
        # Wait for the login form to be present
        self.wait.until(EC.presence_of_element_located(self.EMAIL_INPUT))
        
        # Clear existing values
        self.find_element(*self.EMAIL_INPUT).clear()
        self.find_element(*self.PASSWORD_INPUT).clear()
        
        # Input credentials
        self.input_text(*self.EMAIL_INPUT, email)
        self.input_text(*self.PASSWORD_INPUT, password)
        
        # Click login
        self.click_element(*self.LOGIN_BUTTON)
        
        # Wait a moment for the page to load
        self.driver.implicitly_wait(2)
    
    def get_error_message(self):
        try:
            error_elem = self.wait.until(
                EC.presence_of_element_located(self.ERROR_MESSAGE)
            )
            return error_elem.text
        except:
            return ""
    
    def is_logged_in(self):
        try:
            return "My Account" in self.driver.title
        except:
            return False