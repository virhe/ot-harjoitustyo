import tkinter as tk


class MainWindow:
    def __init__(self, root, user_service):
        self.root = root
        self.root.title("Depysit")
        self.root.geometry("800x600")

        self.user_service = user_service

        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Welcome to Depysit").pack()
