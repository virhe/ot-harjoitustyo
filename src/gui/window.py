import tkinter as tk


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Depysit")
        self.root.geometry("800x600")

        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Welcome to Depysit").pack()
