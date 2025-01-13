import random
import string

class TestData:
    def get_random_string(self, length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    def get_registration_data(self):
        random_email = f"test_{self.get_random_string()}@example.com"
        return {
            "firstname": "Test",
            "lastname": "User",
            "email": random_email,
            "telephone": "1234567890",
            "password": "test123",
            "confirm": "test123"
        }
    
    def get_product_data(self):
        return {
            "search_term": "iPhone",
            "category": "Phones & PDAs",
            "price_min": "100",
            "price_max": "1000"
        }