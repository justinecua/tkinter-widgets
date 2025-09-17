import tkinter as tk
from utils.center_window import center_window
from authActivity.frontend.auth import Auth
from template_widgets.image import create_image_widgets

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Semi Final Examination 2025-2026")
        center_window(self, 800, 800)
        create_image_widgets(self)

def main():
    app = MyApp()
    app.mainloop()

main()
