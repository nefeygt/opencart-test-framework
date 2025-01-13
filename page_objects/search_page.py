from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchPage(BasePage):
    # Updated locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-light.btn-lg")
    PRODUCT_LINKS = (By.CSS_SELECTOR, ".product-thumb h4 a")
    CATEGORY_FILTER = (By.CSS_SELECTOR, "#input-category")
    DESCRIPTION_CHECKBOX = (By.CSS_SELECTOR, "#description")
    SEARCH_IN_DESCRIPTION = (By.NAME, "description")
    
    def search_product(self, product_name):
        self.driver.get("https://demo.opencart.com/index.php?route=product/search")
        time.sleep(2)
        
        search_input = self.wait.until(
            EC.presence_of_element_located(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(product_name)
        
        self.click_element(*self.SEARCH_BUTTON)
        time.sleep(2)
    
    def apply_filter(self, filter_type, filter_value):
        if filter_type.lower() == "category":
            # Click search criteria to expand advanced search
            self.driver.get("https://demo.opencart.com/index.php?route=product/search")
            time.sleep(2)
            
            # Select category
            category_select = Select(self.find_element(*self.CATEGORY_FILTER))
            for option in category_select.options:
                if filter_value.lower() in option.text.lower():
                    category_select.select_by_visible_text(option.text)
                    break
            
            # Check search in description
            self.find_element(*self.SEARCH_IN_DESCRIPTION).click()
            
            # Click search
            self.click_element(*self.SEARCH_BUTTON)
            time.sleep(2)
    
    def get_search_results(self):
        time.sleep(2)  # Wait for results to load
        products = self.driver.find_elements(*self.PRODUCT_LINKS)
        return [product.text for product in products]