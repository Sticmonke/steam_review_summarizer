import unittest
from transformers import pipeline
from reviews_summarizer import steam_review_summarizer

class TestSteamReviewSummarizer(unittest.TestCase):

    def test_summarizer(self):
        processed_reviews = [
            ["don't", "like", "control", "graphic", "amazing"],
            ["never", "played", "better", "game"],
            ["isn't", "fun", "least", "interesting"]
        ]
        
        summary = steam_review_summarizer(processed_reviews)
        
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)
        self.assertLess(len(summary.split()), 50)

if __name__ == '__main__':
    unittest.main()
