import unittest
from nlp_data_processer import process_review_data  # Import your function

class TestReviewPreprocessing(unittest.TestCase):

    def test_process_review_data(self):
        """Test that reviews are tokenized, stopwords are removed, and words are stemmed."""
        
        reviews = [
            "This game is absolutely amazing!",
            "I didn't like the controls, but the graphics are great.",
            "Could have been better, but still enjoyable.",
        ]

        result = process_review_data(reviews)

        # Ensure output is a list of lists
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], list)  # Each review should be its own list of tokens

        # Ensure stopwords are removed
        self.assertNotIn("is", result[0])  # "is" should be removed
        self.assertNotIn("the", result[1])  # "the" should be removed

        # Ensure words are stemmed correctly
        self.assertIn("amaz", result[0])  # "amazing" -> "amaz"
        self.assertIn("graphic", result[1])  # "graphics" -> "graphic"
        self.assertIn("enjoy", result[2])  # "enjoyable" -> "enjoy"

    def test_empty_list(self):
        """Test behavior when an empty list is passed."""
        result = process_review_data([])
        self.assertEqual(result, [])  # Should return an empty list

    def test_single_word_reviews(self):
        """Test behavior with one-word reviews."""
        reviews = ["Amazing!", "Bad", "Great"]
        result = process_review_data(reviews)

        # Ensure each word is stemmed and stays in its own list
        self.assertEqual(result, [["amaz"], ["bad"], ["great"]])

    def test_mixed_case_handling(self):
        """Test case insensitivity in stopword removal."""
        reviews = ["This game IS great."]
        result = process_review_data(reviews)

        # Ensure "is" is removed regardless of case
        self.assertNotIn("is", result[0])
        self.assertIn("game", result[0])  # "game" should remain
        self.assertIn("great", result[0])  # "great" should remain

if __name__ == '__main__':
    unittest.main()
