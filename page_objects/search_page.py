from .base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    # Locators
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn-light")
    PRODUCT_LINKS = (By.CSS_SELECTOR, ".product-thumb h4 a")
    
    def search_product(self, product_name):
        self.input_text(*self.SEARCH_INPUT, product_name)
        self.click_element(*self.SEARCH_BUTTON)
    
    def get_search_results(self):
        products = self.driver.find_elements(*self.PRODUCT_LINKS)
        return [product.text for product in products]