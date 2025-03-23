import unittest
import review_data_scraper
from unittest.mock import patch, MagicMock

class TestStringMethods(unittest.TestCase):

    @patch('review_data_loader.requests.get')
    @unittest.testName('Test load_review_data returns Json')
    def test_load_review_data(self, mock_get):
        
        elden_ring = "1245620"
        params = {
        'json':1,
        'language': 'english',
        'cursor': '*',
        'num_per_page': 100,
        'filter': 'recent'
        }

        # Mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"reviews": ["Good game", "Nice graphics"]}
        
        # Configure the mock to return the mock response
        mock_get.return_value = mock_response
        
        # Call the function with dummy data
        result = review_data_scraper.load_review_data(elden_ring, params)
        
        # Check if the returned result is a valid JSON (a dictionary in this case)
        self.assertIsInstance(result, dict)
        self.assertIn("reviews", result)
        self.assertEqual(result["reviews"], ["Good game", "Nice graphics"])

if __name__ == '__main__':
    unittest.main()