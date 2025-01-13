import pytest
import requests

class TestProductAPI:
    BASE_URL = "https://demo.opencart.com/index.php?route=api/v1"
    
    @pytest.mark.api
    def test_get_product_list(self):
        response = requests.get(f"{self.BASE_URL}/products")
        assert response.status_code == 200
        data = response.json()
        assert "products" in data
    
    @pytest.mark.api
    def test_get_product_details(self):
        product_id = 42
        response = requests.get(f"{self.BASE_URL}/products/{product_id}")
        assert response.status_code == 200
        data = response.json()
        assert "product_id" in data