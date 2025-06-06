print("main_gui.py is imported")

import tkinter as tk
from tkinter import filedialog, messagebox

class Analysis:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Analyzer - Input")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        # Title Label
        title_label = tk.Label(
            root,
            text="Text Analyzer",
            font=("Helvetica", 16, "bold")
        )
        title_label.pack(pady=10)

        # File selection
        self.label = tk.Label(root, text="Choose a text file:")
        self.label.pack(pady=5)

        self.file_button = tk.Button(
            root, text="Browse", command=self.load_file
        )
        self.file_button.pack()

        self.file_path = tk.StringVar()
        self.file_display = tk.Label(
            root, textvariable=self.file_path, fg="blue", wraplength=400
        )
        self.file_display.pack(pady=5)

        # Keyword input
        self.keyword_label = tk.Label(
            root, text="Enter keywords to search (comma separated):"
        )
        self.keyword_label.pack(pady=10)

        self.keyword_entry = tk.Entry(root, width=50)
        self.keyword_entry.pack()

        # Submit button
        self.submit_button = tk.Button(
            root, text="Analyze", command=self.submit
        )
        self.submit_button.pack(pady=20)

    def load_file(self):
        filetypes = [("Text files", "*.txt"), ("All files", "*.*")]
        filename = filedialog.askopenfilename(
            title="Open file", filetypes=filetypes
        )
        if filename:
            self.file_path.set(filename)

    def submit(self):
        file = self.file_path.get()
        keywords = self.keyword_entry.get()

        if not file:
            messagebox.showerror("Error", "No file selected.")
            return

        if not keywords:
            messagebox.showerror("Error", "Please enter at least one keyword.")
            return

        try:
            import results_gui
            self.root.destroy()
            results_gui.display_results(file, keywords.split(","))
        except ImportError as e:
            messagebox.showerror("Import Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Entry point for running this file independently (optional)
if __name__ == "__main__":
    root = tk.Tk()
    app = Analysis(root)
    root.mainloop()

print(dir())
