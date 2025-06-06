import tkinter as tk
import main_gui

def main():
    root = tk.Tk()
    app = main_gui.Analysis(root)
    root.mainloop()

if __name__ == "__main__":
    main()