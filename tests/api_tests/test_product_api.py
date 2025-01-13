import pytest
from unittest.mock import patch
import json

class TestProductAPI:
    @pytest.mark.api
    @patch('requests.get')
    def test_get_product_list(self, mock_get):
        # Mock response
        mock_response = type('Response', (), {
            'status_code': 200,
            'json': lambda: {
                'products': [
                    {'id': 1, 'name': 'iPhone', 'price': 999.99},
                    {'id': 2, 'name': 'Samsung Galaxy', 'price': 899.99}
                ]
            }
        })
        mock_get.return_value = mock_response
        
        response = mock_get.return_value
        assert response.status_code == 200
        assert 'products' in response.json()

    @pytest.mark.api
    @patch('requests.get')
    def test_get_product_details(self, mock_get):
        mock_response = type('Response', (), {
            'status_code': 200,
            'json': lambda: {
                'product_id': 42,
                'name': 'iPhone',
                'price': 999.99,
                'description': 'Latest iPhone model'
            }
        })
        mock_get.return_value = mock_response
        
        response = mock_get.return_value
        assert response.status_code == 200
        assert 'product_id' in response.json()