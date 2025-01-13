import pytest
from page_objects.login_page import LoginPage

class TestLogin:
    @pytest.mark.ui
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        driver.get("https://demo.opencart.com/index.php?route=account/login")
        login_page.login("demo@opencart.com", "demo123")
        assert "My Account" in driver.title
    
    @pytest.mark.ui
    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        driver.get("https://demo.opencart.com/index.php?route=account/login")
        login_page.login("wrong@email.com", "wrongpass")
        assert "Warning: No match" in login_page.get_error_message()