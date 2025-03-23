import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

def process_review_data(steam_reviews: list) -> list:

    """
    Preprocesses the given list of Steam reviews by performing tokenization, stopword removal, and stemming.

    Parameters:
    steam_reviews (list): A list of Steam reviews (strings) to be processed.

    Returns:
    list: A list of stemmed tokens (words) after preprocessing.
    """

    # Standard stopwords but keeping negations
    stop_words = set(stopwords.words('english')) - {"not", "no", "nor", "isn't", "wasn't", "aren't", "weren't", 
                                                     "doesn't", "don't", "didn't", "haven't", "hasn't", "won't", 
                                                     "wouldn't", "shouldn't", "can't", "couldn't", "mustn't"}

    # Tokenizer that keeps contractions (isn't → isn't, don't → don't)
    tokenizer = RegexpTokenizer(r"\b\w+(?:'\w+)?\b")  
    ps = PorterStemmer()

    processed_reviews = []

    for review in steam_reviews:
        tokens = tokenizer.tokenize(review.lower())  # Lowercase + tokenize
        filtered_tokens = [word for word in tokens if word not in stop_words]  # Remove only unimportant words
        stemmed_tokens = [ps.stem(word) for word in filtered_tokens]  # Apply stemming

        processed_reviews.append(stemmed_tokens)

    return processed_reviews

if __name__ == '__main__':
    None