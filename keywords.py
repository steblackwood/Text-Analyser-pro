import re
from collections import Counter

def find_keywords(text, keywords):
    """
    Counts the occurrences of each keyword in the given text.
    
    Args:
        text (str): The input text.
        keywords (list): List of keywords to search for.
        
    Returns:
        dict: Dictionary with keyword as key and count as value.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    keyword_counts = {}

    for keyword in keywords:
        keyword_lower = keyword.strip().lower()
        keyword_counts[keyword_lower] = word_counts.get(keyword_lower, 0)

    return keyword_counts
