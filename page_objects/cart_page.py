from .base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    # Locators
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a.btn-primary[href*='checkout']")
    CART_ITEMS = (By.CSS_SELECTOR, "table.table-bordered tbody tr")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input[name^='quantity']")
    UPDATE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Update']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Remove']")

    def proceed_to_checkout(self):
        # Wait for cart page to load and click checkout
        self.click_element(*self.CHECKOUT_BUTTON)

    def update_quantity(self, product_index, quantity):
        items = self.driver.find_elements(*self.CART_ITEMS)
        if product_index < len(items):
            quantity_input = items[product_index].find_element(*self.QUANTITY_INPUT)
            quantity_input.clear()
            quantity_input.send_keys(str(quantity))
            items[product_index].find_element(*self.UPDATE_BUTTON).click()

    def remove_item(self, product_index):
        items = self.driver.find_elements(*self.CART_ITEMS)
        if product_index < len(items):
            items[product_index].find_element(*self.REMOVE_BUTTON).click()