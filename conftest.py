import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    # Add options for stability
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
    except Exception as e:
        print(f"Error initializing Chrome driver: {e}")
        # Try alternative setup
        driver = webdriver.Chrome(options=chrome_options)
    
    driver.implicitly_wait(10)
    yield driver
    driver.quit()