import re
from collections import Counter

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return len(words)

def count_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])

def most_frequent_words(text, n=5):
    words = re.findall(r'\b\w+\b', text.lower())
    frequency = Counter(words)
    return frequency.most_common(n)

def average_word_length(text):
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return round(total_length / len(words), 2)

def analyze_text(text):
    word_count = count_words(text)
    sentence_count = count_sentences(text)
    most_common = most_frequent_words(text, n=10)
    avg_word_length = average_word_length(text)
    
    return word_count, sentence_count, most_common, avg_word_length

