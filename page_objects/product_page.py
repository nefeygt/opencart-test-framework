from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage(BasePage):
    # Updated locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-light.btn-lg")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[onclick*='cart.add']")
    CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")

    def search_product(self, product_name):
        self.driver.get("https://demo.opencart.com/")
        time.sleep(2)  # Wait for page load
        
        # Ensure search field is visible
        search_input = self.wait.until(
            EC.presence_of_element_located(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(product_name)
        
        # Click search
        self.click_element(*self.SEARCH_BUTTON)
        time.sleep(2)  # Wait for results

    def add_to_cart(self, product_name):
        # Click add to cart for the first product
        add_to_cart_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if add_to_cart_buttons:
            add_to_cart_buttons[0].click()
            time.sleep(1)  # Wait for cart update
            
            # Wait for success message
            self.wait.until(
                EC.presence_of_element_located(self.SUCCESS_ALERT)
            )
        else:
            raise Exception("No products found to add to cart")