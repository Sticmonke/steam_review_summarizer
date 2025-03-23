
# Steam Review Summarizer

## Overview

This project processes Steam game reviews, cleans them using NLP techniques, and generates concise summaries. It uses the Hugging Face transformer model (`t5-small`) for text summarization and NLTK for preprocessing.

## Features

- **Fetch Steam Reviews**: Fetches reviews for a specific game using the Steam API.
- **Preprocessing**: Tokenizes reviews, removes stopwords, and performs stemming using NLTK.
- **Summarization**: Uses Hugging Face's `t5-small` model to summarize the reviews.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. **Environment Variables**:  
   Create a `.env` file in the project root directory with your Steam API key.  
   Example `.env` file:
   ```
   STEAM_API_KEY=your_steam_api_key
   ```

### `.env` file

```
STEAM_API_KEY=your_steam_api_key
```

### `requirements.txt`

```
nltk==3.6.3
requests==2.25.1
transformers==4.11.3
torch==1.10.0
python-dotenv==0.19.2
```

## Testing

You can run the unit tests with:
```
python -m unittest discover
```

## License

This project is open-source under the MIT License.
