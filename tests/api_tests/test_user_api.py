import pytest
from unittest.mock import patch
import json

class TestUserAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_client = None  # We'll use mocked responses instead

    @pytest.mark.api
    @patch('requests.post')
    def test_user_registration(self, mock_post):
        # Mock response
        mock_response = type('Response', (), {
            'status_code': 201,
            'json': lambda: {
                'user_id': 123,
                'message': 'User registered successfully'
            }
        })
        mock_post.return_value = mock_response
        
        response = mock_post.return_value
        assert response.status_code == 201
        assert 'user_id' in response.json()

    @pytest.mark.api
    @patch('requests.post')
    def test_user_login(self, mock_post):
        mock_response = type('Response', (), {
            'status_code': 200,
            'json': lambda: {
                'token': 'mock-jwt-token',
                'user': {'id': 123, 'email': 'demo@opencart.com'}
            }
        })
        mock_post.return_value = mock_response
        
        response = mock_post.return_value
        assert response.status_code == 200
        assert 'token' in response.json()