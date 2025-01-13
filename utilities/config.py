class Config:
    # Base URLs
    BASE_URL = "https://demo.opencart.com"
    API_BASE_URL = "https://demo.opencart.com/index.php?route=api/v1"
    
    # Test Users
    TEST_USER = {
        "email": "demo@opencart.com",
        "password": "demo123"
    }
    
    # Timeouts
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    
    # Browser
    BROWSER = "chrome"
    HEADLESS = False