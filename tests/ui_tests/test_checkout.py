import pytest
from page_objects.product_page import ProductPage
from page_objects.cart_page import CartPage
from page_objects.checkout_page import CheckoutPage
import time

class TestCheckout:
    @pytest.mark.ui
    def test_complete_checkout_process(self, driver):
        # Navigate to home page first
        driver.get("https://demo.opencart.com/")
        time.sleep(2)  # Wait for page load
        
        # Initialize pages
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        
        # Search and add product to cart
        product_page.search_product("iPhone")
        product_page.add_to_cart("iPhone")
        
        # Proceed to checkout
        cart_page.proceed_to_checkout()
        
        # Fill checkout details
        checkout_page.fill_billing_details({
            "firstname": "John",
            "lastname": "Doe",
            "email": "john.doe@example.com",
            "telephone": "1234567890",
            "address_1": "123 Test Street",
            "city": "Test City",
            "postcode": "12345",
            "country": "Finland",
            "region": "Uusimaa"
        })
        
        # Complete order
        checkout_page.confirm_order()
        assert "Your order has been placed!" in checkout_page.get_success_message()