import pytest
from page_objects.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestLogin:
    @pytest.mark.ui
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        # Use the full URL including route
        driver.get("https://demo.opencart.com/index.php?route=account/login")
        
        # Wait for page to load completely
        time.sleep(2)
        
        login_page.login("demo@opencart.com", "demo123")
        
        # Wait for redirect and check title
        WebDriverWait(driver, 10).until(
            lambda x: "My Account" in x.title
        )
        assert "My Account" in driver.title
    
    @pytest.mark.ui
    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        driver.get("https://demo.opencart.com/index.php?route=account/login")
        
        # Wait for page to load completely
        time.sleep(2)
        
        login_page.login("wrong@email.com", "wrongpass")
        
        # Wait for error message
        error_message = login_page.get_error_message()
        assert "Warning" in error_message