import unittest
from unittest.mock import patch
from forex import is_valid_currency, is_valid_amount, get_converted_amount


class TestForexFunctions(unittest.TestCase):
    def test_is_valid_currency(self):
        self.assertTrue(is_valid_currency("USD"))
        self.assertTrue(is_valid_currency("usd"))
        self.assertTrue(is_valid_currency("EUR"))
        self.assertFalse(is_valid_currency("US"))
        self.assertFalse(is_valid_currency("USDFNBDJSK"))
    
    def test_is_valid_amount(self):
        self.assertTrue(is_valid_amount(1))
        self.assertTrue(is_valid_amount(50))
        self.assertFalse(is_valid_amount(-50))
        self.assertFalse(is_valid_amount(0))
        self.assertFalse(is_valid_amount("abc"))

    @patch('forex.requests.get')
    def test_get_converted_amount(self, mock_get):
        mock_response = {
            'result':1,
            'query': {'to': 'USD'}
        }

        mock_get.return_value.json.return_value = mock_response

        converted_amount, symbol = get_converted_amount('usd', 'usd', 1)

        self.assertTrue(converted_amount, 1)
        self.assertTrue(symbol, 'usd')