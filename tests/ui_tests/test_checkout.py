import pytest
from page_objects.product_page import ProductPage
from page_objects.cart_page import CartPage
from page_objects.checkout_page import CheckoutPage

class TestCheckout:
    @pytest.mark.ui
    def test_complete_checkout_process(self, driver):
        # Add a product to cart
        product_page = ProductPage(driver)
        product_page.add_to_cart("iPhone")
        
        # Go to cart and proceed
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()
        
        # Complete checkout
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_billing_details()
        checkout_page.confirm_order()
        
        assert "Your order has been placed!" in checkout_page.get_success_message()