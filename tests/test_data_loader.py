import unittest
from review_data_scraper import *
from unittest.mock import patch, MagicMock

class TestDataScraper(unittest.TestCase):

    @patch('review_data_scraper.requests.get')
    @patch('review_data_scraper.os.getenv', return_value="mocked_key")
    def test_load_review_data(self, mock_getenv, mock_get):
        
        #example mock data
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
        result = load_review_data(elden_ring, params)
        
        # Check if the returned result is a valid JSON (a dictionary in this case)
        self.assertIsInstance(result, dict)
        self.assertIn("reviews", result)
        self.assertEqual(result["reviews"], ["Good game", "Nice graphics"])

    def test_retrieve_reviews_empty(self):
        response = {"success": True, "reviews": []}
        result = retrieve_reviews(response)
        self.assertEqual(result, [])  # Should return an empty list

    def test_retrieve_reviews(self):
        # Example response to test the function
        response = {
            "success": True,
            "query_summary": {
                "num_reviews": 1000,
                "review_score": 85
            },
            "reviews": [
                {
                    "review": "Great game! Highly recommend.",
                    "author": {
                        "steamid": "12345",
                        "num_games_owned": 50
                    },
                    "timestamp_created": 1609459200,
                    "voted_up": True
                },
                {
                    "review": "Not bad, but could be improved.",
                    "author": {
                        "steamid": "67890",
                        "num_games_owned": 20
                    },
                    "timestamp_created": 1609545600,
                    "voted_up": True
                }
            ]
        }
        
        # Call the function
        result = retrieve_reviews(response)
        
        # Expected result
        expected = [
            "Great game! Highly recommend.",
            "Not bad, but could be improved."
        ]
        
        # Assert that the result matches the expected outcome
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()