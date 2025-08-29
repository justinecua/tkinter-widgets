import tkinter as tk
from utils.center_window import center_window
from widgets.hello import hello

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Label Demo")
        self.configure(bg="#2c3e50")

        center_window(self, 800, 800)
        hello(self)

def main():
    app = MyApp()
    app.mainloop()

main()
