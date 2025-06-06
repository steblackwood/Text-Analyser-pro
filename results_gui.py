import tkinter as tk
from tkinter import scrolledtext

def display_results(file_path, keywords):
    # Import analysis modules here to avoid circular imports
    import core
    import sentiment
    import keywords as kw

    # Read file content
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Perform analyses
    word_count = core.count_words(text)
    sentence_count = core.count_sentences(text)
    most_freq = core.most_frequent_words(text)
    avg_word_len = core.average_word_length(text)
    sentiment_result = sentiment.analyze_sentiment(text)
    keywords_found = kw.find_keywords(text, keywords)

    # Create the results window
    root = tk.Tk()
    root.title("Text Analyzer - Results")
    root.geometry("700x600")
    root.configure(bg="#f4f4f4")
    root.resizable(False, False)

    # Title label
    title_label = tk.Label(
        root,
        text="Analysis Results",
        font=("Segoe UI", 20, "bold"),
        bg="#f4f4f4",
        fg="#333"
    )
    title_label.pack(pady=20)

    # Frame for stats
    stats_frame = tk.Frame(root, bg="#f4f4f4")
    stats_frame.pack(pady=10, padx=20, fill='x')

    # Stats labels
    stats = {
        "Word Count": word_count,
        "Sentence Count": sentence_count,
        "Average Word Length": avg_word_len,
        "Sentiment": sentiment_result
    }

    for key, val in stats.items():
        label = tk.Label(
            stats_frame,
            text=f"{key}: {val}",
            font=("Segoe UI", 14),
            bg="#f4f4f4",
            anchor="w"
        )
        label.pack(fill='x', pady=2)

    # Most frequent words
    freq_label = tk.Label(
        root,
        text="Most Frequent Words:",
        font=("Segoe UI", 16, "bold"),
        bg="#f4f4f4",
        fg="#444"
    )
    freq_label.pack(pady=(20, 5), anchor='w', padx=20)

    freq_words_text = ', '.join([f"{word} ({count})" for word, count in most_freq])
    freq_words_label = tk.Label(
        root,
        text=freq_words_text,
        font=("Segoe UI", 12),
        bg="#f4f4f4",
        wraplength=650,
        justify="left"
    )
    freq_words_label.pack(padx=20)

    # Keywords found
    keyword_label = tk.Label(
        root,
        text="Keywords Found:",
        font=("Segoe UI", 16, "bold"),
        bg="#f4f4f4",
        fg="#444"
    )
    keyword_label.pack(pady=(20, 5), anchor='w', padx=20)

    keywords_text = ', '.join(keywords_found) if keywords_found else "No keywords found."
    keywords_found_label = tk.Label(
        root,
        text=keywords_text,
        font=("Segoe UI", 12),
        bg="#f4f4f4",
        wraplength=650,
        justify="left"
    )
    keywords_found_label.pack(padx=20)

    # Text content preview
    preview_label = tk.Label(
        root,
        text="Text Preview:",
        font=("Segoe UI", 16, "bold"),
        bg="#f4f4f4",
        fg="#444"
    )
    preview_label.pack(pady=(20, 5), anchor='w', padx=20)

    text_preview = scrolledtext.ScrolledText(
        root,
        width=80,
        height=15,
        font=("Segoe UI", 11),
        bg="white",
        fg="#222",
        wrap=tk.WORD
    )
    text_preview.pack(padx=20, pady=(0, 20))
    text_preview.insert(tk.END, text[:2000] + ("..." if len(text) > 2000 else ""))
    text_preview.config(state=tk.DISABLED)  # Make read-only

    root.mainloop()
