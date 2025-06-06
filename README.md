Text Analyzer Pro

Text Analyzer Pro is a modular Python application with a user-friendly graphical interface. It allows users to upload text files, enter custom keywords, and receive detailed text analysis results — including sentiment detection, word frequency, and more.

---

Features

- Upload `.txt` files via the GUI
- Analyze and display:
  - Total word count
  - Sentence count
  - Most frequent words
  - Average word length
- Custom keyword detection (entered by the user)
- Sentiment analysis using `TextBlob`
- Clean, interactive GUI built with `tkinter`
- Modular structure for easy maintenance and future expansion

---

Demo

> Coming Soon: Screenshots and a short walkthrough GIF will be added here.

---

Installation

1. Clone the repository
   git clone https://github.com/yourusername/text-analyzer-pro.git
   cd text-analyzer-pro

2. Install dependencies
   pip install -r requirements.txt

3. Run the application
   python run.py

---

Directory Structure

text-analyzer-pro/
├── analyzer/
│   ├── core.py            # Core analysis functions
│   ├── sentiment.py       # Sentiment analysis logic
│   ├── keywords.py        # Keyword detection
├── gui/
│   ├── main_gui.py        # GUI input screen
│   ├── results_gui.py     # GUI output display
├── assets/
│   └── sample.txt         # Example input file
├── run.py                 # Main application launcher
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

---

Requirements

- Python 3.8 or above
- textblob
- nltk
- tkinter (usually pre-installed with Python)

To install all dependencies:
pip install -r requirements.txt

Note: You may need to download NLTK corpora if prompted.

---

Future Improvements

- Export results to PDF/CSV
- Batch file processing
- Light/Dark mode toggle
- Web-based version (Flask or Streamlit)

---

License

This project is provided for personal and educational use. Unauthorized redistribution, resale, or code extraction for commercial use is prohibited.

© 2025 Stephen Blackwood. All rights reserved.
