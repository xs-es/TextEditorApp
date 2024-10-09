import json

class ThemeManager:
    def __init__(self, editor):
        self.editor = editor

    def load_theme(self, theme_file, theme_name):
        try:
            with open(theme_file, 'r') as file:
                data = json.load(file)
                # Find the theme by name
                theme = next((item['properties'] for item in data if item['theme'] == theme_name), None)
                if theme:
                    self.editor.apply_theme(theme)
                    print(f"Theme '{theme_name}' applied successfully.")
                else:
                    print(f"Error: Theme '{theme_name}' not found in {theme_file}.")
        except FileNotFoundError:
            print(f"Error: Theme file '{theme_file}' not found.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in theme file '{theme_file}'.")
