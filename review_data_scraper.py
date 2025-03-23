from dotenv import load_dotenv
import os
import requests
from typing import Dict

load_dotenv()
steam_api_key = os.getenv("STEAM_API_KEY")

def load_review_data (game_id: str, params: Dict) -> Dict:

    """
    Fetches game review data from Steam's API.

    Parameters:
    game_id (str): The Steam game ID.
    params (dict): Query parameters for the API request (e.g., language, num_per_page).

    Returns:
    dict: The JSON response from the API, containing review data or an error message.
    """

    reviews_url = f'https://store.steampowered.com/appreviews/{game_id}'

    # Add the API key to the params
    params['key'] = steam_api_key
    
    user_reviews = requests.get(
        reviews_url,
        params=params
    )

    if user_reviews.status_code != 200:
        print(f'Response failed. Status code: {user_reviews.status_code}')
        return {"success": 2}
    
    try:
        user_reviews = user_reviews.json()
    except:
        return {"success": 2}

    return user_reviews

def retrieve_reviews (review_data: Dict) -> list:

    """
    Extracts the list of reviews from a dictionary of review data.

    Parameters:
    review_data (Dict): A dictionary containing review data, expected to have a 'reviews' key with a list of reviews.

    Returns:
    list: A list of reviews (strings) extracted from the 'reviews' key in the input dictionary.
    """
    
    review_list = [review['review'] for review in review_data['reviews']]

    return review_list

if __name__ == '__main__':
    None