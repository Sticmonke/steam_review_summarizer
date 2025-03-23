from transformers import pipeline

# Load Hugging Face summarization model
summarizer = pipeline("summarization", model="t5-small")

def steam_review_summarizer(processed_reviews: list) -> str:
    """
    Summarizes the given processed reviews using Hugging Face's T5 model.
    
    Parameters:
    processed_reviews (list): A list of tokenized and pre-processed reviews (list of strings).
    
    Returns:
    str: A concise summary of the reviews.
    """
    
    # Join the tokenized reviews into sentences and combine all sentences into one large text
    review_sentences = [" ".join(tokens) for tokens in processed_reviews]
    full_text = " ".join(review_sentences)
    
    # If there are no reviews, return a message
    if not full_text:
        return "No reviews available to summarize."

    try:
        # Get the summary from the model (control the length of the summary)
        final_summary = summarizer(full_text, max_length=50, min_length=30, do_sample=False)
        return final_summary[0]['summary_text']
    except Exception as e:
        return f"An error occurred while generating the summary: {str(e)}"