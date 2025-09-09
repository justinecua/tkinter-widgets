import tkinter as tk
from utils.center_window import center_window
from authActivity.frontend.auth import Auth

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Label Demo")
        center_window(self, 800, 800)
        Auth(self)

def main():
    app = MyApp()
    app.mainloop()

main()
