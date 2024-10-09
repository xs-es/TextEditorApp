import tkinter as tk
from tkinter import font, filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(root, wrap="word", undo=True)
        self.text_area.pack(expand=True, fill='both')

        # Set default fonts
        self.default_font = font.Font(family="Arial", size=12)
        self.title_font = font.Font(family="Arial", size=24, weight="bold")
        self.subtitle_font = font.Font(family="Arial", size=18, slant="italic")

        self.text_area.tag_configure("title", font=self.title_font)
        self.text_area.tag_configure("subtitle", font=self.subtitle_font)
        self.text_area.tag_configure("maintext", font=self.default_font)

    def auto_format(self):
        # Example of auto-formatting by detecting section keywords and cleaning up unwanted characters
        text = self.text_area.get(1.0, tk.END)
        self.text_area.delete(1.0, tk.END)
        
        lines = text.split("\n")
        for line in lines:
            cleaned_line = self._clean_text(line)
            if "#Title" in line:
                self.text_area.insert(tk.END, cleaned_line.replace("#Title", ""), "title")
            elif "#Subtitle" in line:
                self.text_area.insert(tk.END, cleaned_line.replace("#Subtitle", ""), "subtitle")
            else:
                self.text_area.insert(tk.END, cleaned_line, "maintext")

    def _clean_text(self, text):
        # Remove unwanted characters such as #, * and extra spaces
        return text.replace("#", "").replace("*", "").strip()

    def apply_theme(self, theme):
        # Apply theme settings
        self.text_area.config(bg=theme["background"], fg=theme["fontColor"])
        self.title_font.config(family=theme["titleFont"], size=theme["titleSize"], weight="bold")
        self.subtitle_font.config(family=theme["subtitleFont"], size=theme["subtitleSize"], slant="italic")
        self.default_font.config(family=theme["fontFamily"], size=theme["fontSize"])

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
