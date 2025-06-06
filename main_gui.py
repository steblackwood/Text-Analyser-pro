import tkinter as tk
from tkinter import filedialog, messagebox

class Analysis:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Analyzer")
        self.root.geometry("600x400")
        self.root.configure(bg="#f4f4f4")
        self.root.resizable(False, False)

        # ===== Title =====
        title_label = tk.Label(
            root,
            text="Text Analyzer",
            font=("Segoe UI", 20, "bold"),
            bg="#f4f4f4",
            fg="#333"
        )
        title_label.pack(pady=20)

        # ===== File Selection =====
        file_frame = tk.Frame(root, bg="#f4f4f4")
        file_frame.pack(pady=10)

        file_label = tk.Label(
            file_frame,
            text="Choose a text file:",
            font=("Segoe UI", 12),
            bg="#f4f4f4"
        )
        file_label.pack(side=tk.LEFT, padx=5)

        file_button = tk.Button(
            file_frame,
            text="Browse",
            font=("Segoe UI", 10),
            command=self.load_file,
            bg="#3498db",
            fg="white",
            relief=tk.FLAT,
            padx=10
        )
        file_button.pack(side=tk.LEFT)

        self.file_path = tk.StringVar()
        self.file_display = tk.Label(
            root,
            textvariable=self.file_path,
            fg="blue",
            bg="#f4f4f4",
            font=("Segoe UI", 10),
            wraplength=500
        )
        self.file_display.pack(pady=5)

        # ===== Keywords Entry =====
        keyword_label = tk.Label(
            root,
            text="Enter keywords to search (comma separated):",
            font=("Segoe UI", 12),
            bg="#f4f4f4"
        )
        keyword_label.pack(pady=(20, 5))

        self.keyword_entry = tk.Entry(
            root,
            width=50,
            font=("Segoe UI", 10)
        )
        self.keyword_entry.pack(pady=5)

        # ===== Submit Button =====
        submit_button = tk.Button(
            root,
            text="Analyze",
            font=("Segoe UI", 11, "bold"),
            bg="#27ae60",
            fg="white",
            relief=tk.FLAT,
            command=self.submit,
            padx=15,
            pady=5
        )
        submit_button.pack(pady=20)

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


if __name__ == "__main__":
    root = tk.Tk()
    app = Analysis(root)
    root.mainloop()
