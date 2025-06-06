import tkinter as tk
from tkinter import ttk, scrolledtext
from core import count_words, count_sentences, most_frequent_words, average_word_length
from sentiment import analyze_sentiment
from keywords import find_keywords

def display_results(file_path, keywords):
    # Read the file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print("Error reading file:", e)
        return

    # Run analysis
    word_count = count_words(text)
    sentence_count = count_sentences(text)
    frequent_words = most_frequent_words(text)
    avg_word_length = average_word_length(text)
    sentiment = analyze_sentiment(text)
    keyword_data = find_keywords(text, keywords)

    # Create results window
    root = tk.Tk()
    root.title("Text Analyzer - Results")
    root.geometry("600x500")

    title = tk.Label(root, text="Analysis Results", font=("Helvetica", 16, "bold"))
    title.pack(pady=10)

    # Use a scrolled text box to show results
    result_box = scrolledtext.ScrolledText(root, width=70, height=25, wrap=tk.WORD)
    result_box.pack(padx=10, pady=10)

    result_box.insert(tk.END, f"Total Words: {word_count}\n")
    result_box.insert(tk.END, f"Total Sentences: {sentence_count}\n")
    result_box.insert(tk.END, f"Average Word Length: {avg_word_length}\n\n")

    result_box.insert(tk.END, "Most Frequent Words:\n")
    for word, count in frequent_words:
        result_box.insert(tk.END, f"  {word}: {count}\n")

    result_box.insert(tk.END, "\nSentiment Analysis:\n")
    result_box.insert(tk.END, f"  Polarity: {sentiment['polarity']}\n")
    result_box.insert(tk.END, f"  Subjectivity: {sentiment['subjectivity']}\n")

    result_box.insert(tk.END, "\nKeyword Counts:\n")
    for word, count in keyword_data.items():
        result_box.insert(tk.END, f"  {word}: {count}\n")

    result_box.config(state=tk.DISABLED)

    root.mainloop()
