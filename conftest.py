import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="function")
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--headless")  # Run in headless mode for stability
    
    try:
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()),
            options=firefox_options
        )
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
    finally:
        if driver:
            driver.quit()