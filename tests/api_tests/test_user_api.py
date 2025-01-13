import pytest
import requests
from utilities.api_client import APIClient
from utilities.test_data import TestData

class TestUserAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_client = APIClient()
        self.test_data = TestData()

    @pytest.mark.api
    def test_user_registration(self):
        payload = self.test_data.get_registration_data()
        response = self.api_client.post("/register", json=payload)
        assert response.status_code == 201
        assert "user_id" in response.json()

    @pytest.mark.api
    def test_user_login(self):
        payload = {
            "email": "demo@opencart.com",
            "password": "demo123"
        }
        response = self.api_client.post("/login", json=payload)
        assert response.status_code == 200
        assert "token" in response.json()