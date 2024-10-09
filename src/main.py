import tkinter as tk
from tkinter import filedialog
from text_editor import TextEditor
from theme_manager import ThemeManager

def run_text_editor():
    root = tk.Tk()
    root.title("Advanced Text Editor with Auto-Formatting")
    root.geometry("800x600")

    editor = TextEditor(root)
    theme_manager = ThemeManager(editor)

    # Menu for file operations and theme application
    menubar = tk.Menu(root)
    
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Open", command=editor.open_file)
    file_menu.add_command(label="Save", command=editor.save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)

    theme_menu = tk.Menu(menubar, tearoff=0)
    theme_menu.add_command(label="Apply Neon Lights Theme", command=lambda: theme_manager.load_theme('../themes/themes.json', 'neonlights'))
    theme_menu.add_command(label="Apply Glow Theme", command=lambda: theme_manager.load_theme('../themes/themes.json', 'glow'))
    menubar.add_cascade(label="Themes", menu=theme_menu)

    format_menu = tk.Menu(menubar, tearoff=0)
    format_menu.add_command(label="Auto-Format", command=editor.auto_format)
    menubar.add_cascade(label="Format", menu=format_menu)

    root.config(menu=menubar)
    root.mainloop()

if __name__ == '__main__':
    run_text_editor()
