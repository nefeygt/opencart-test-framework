from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(BasePage):
    # Locators
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn-light")
    PRODUCT_LINKS = (By.CSS_SELECTOR, ".product-thumb h4 a")
    CATEGORY_DROPDOWN = (By.NAME, "category_id")
    SEARCH_CRITERIA = (By.ID, "input-search")
    SUBCATEGORY_CHECKBOX = (By.NAME, "sub_category")
    DESCRIPTION_CHECKBOX = (By.ID, "description")
    
    def search_product(self, product_name):
        # Clear any existing search first
        search_input = self.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        # Perform search
        self.input_text(*self.SEARCH_INPUT, product_name)
        self.click_element(*self.SEARCH_BUTTON)
    
    def apply_filter(self, filter_type, filter_value):
        if filter_type.lower() == "category":
            # Wait for category dropdown to be present
            category_select = Select(self.find_element(*self.CATEGORY_DROPDOWN))
            # Find the option that contains the text (partial match)
            for option in category_select.options:
                if filter_value in option.text:
                    category_select.select_by_visible_text(option.text)
                    break
            
            # Check subcategories
            self.find_element(*self.SUBCATEGORY_CHECKBOX).click()
            
            # Click search again to apply filters
            self.click_element(*self.SEARCH_BUTTON)
    
    def get_search_results(self):
        # Wait for results to load
        self.wait.until(EC.presence_of_element_located(self.PRODUCT_LINKS))
        products = self.driver.find_elements(*self.PRODUCT_LINKS)
        return [product.text for product in products]

    def get_no_results_message(self):
        try:
            no_results = self.find_element(By.CSS_SELECTOR, "#content p")
            return no_results.text
        except:
            return ""