from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of the text.
    
    Args:
        text (str): Input text.
        
    Returns:
        dict: Sentiment polarity and subjectivity scores.
            - polarity: float [-1.0 (negative) to 1.0 (positive)]
            - subjectivity: float [0.0 (objective) to 1.0 (subjective)]
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment
    
    return {
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity
    }