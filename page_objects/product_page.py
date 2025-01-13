from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    # Locators
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn-default")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[onclick*='cart.add']")
    CART_TOTAL = (By.ID, "cart-total")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")

    def add_to_cart(self, product_name):
        # Search for the product first
        self.input_text(*self.SEARCH_INPUT, product_name)
        self.click_element(*self.SEARCH_BUTTON)
        
        # Add first result to cart
        self.click_element(*self.ADD_TO_CART_BUTTON)
        
        # Wait for success message
        success_message = self.find_element(*self.SUCCESS_ALERT)
        assert "Success" in success_message.text
        
        # Click on cart total to view cart
        self.click_element(*self.CART_TOTAL)