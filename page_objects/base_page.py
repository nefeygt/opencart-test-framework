from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Increased timeout
    
    def find_element(self, by, value):
        try:
            logger.info(f"Finding element with locator: {by}={value}")
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            logger.info("Element found successfully")
            return element
        except TimeoutException as e:
            logger.error(f"TimeoutException finding element: {by}={value}")
            logger.error(f"Current URL: {self.driver.current_url}")
            logger.error(f"Page source: {self.driver.page_source[:500]}...")  # Log first 500 chars of page source
            raise e
    
    def click_element(self, by, value):
        try:
            logger.info(f"Attempting to click element: {by}={value}")
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
            logger.info("Element clicked successfully")
        except Exception as e:
            logger.error(f"Error clicking element: {by}={value}")
            logger.error(f"Error details: {str(e)}")
            raise e
    
    def input_text(self, by, value, text):
        try:
            logger.info(f"Inputting text into element: {by}={value}")
            element = self.find_element(by, value)
            element.clear()
            element.send_keys(text)
            logger.info(f"Text input successful: {text}")
        except Exception as e:
            logger.error(f"Error inputting text: {by}={value}, text={text}")
            logger.error(f"Error details: {str(e)}")
            raise e

    def wait_for_url_contains(self, text, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
        except TimeoutException:
            logger.error(f"Timeout waiting for URL to contain: {text}")
            logger.error(f"Current URL: {self.driver.current_url}")
            return False

    def wait_for_title_contains(self, text, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.title_contains(text)
            )
        except TimeoutException:
            logger.error(f"Timeout waiting for title to contain: {text}")
            logger.error(f"Current title: {self.driver.title}")
            return False