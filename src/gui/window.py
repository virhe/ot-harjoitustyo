import tkinter as tk
from tkinter import Toplevel


class MainWindow:
    def __init__(self, root, user_service):
        self.root = root
        self.root.title("Depysit")
        self.root.geometry("800x600")

        self.user_service = user_service

        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Welcome to Depysit").pack()


class ComboForm(Toplevel):
    def __init__(self, root, user_service):
        super().__init__(root)
        self.user_service = user_service
        self.title("Login/Register")

        tk.Label(self, text="Username:").pack()
        self.username = tk.Entry(self)
        self.username.pack()

        tk.Label(self, text="Password:").pack()
        self.password = tk.Entry(self, show="*")
        self.password.pack()

        login_button = tk.Button(self, text="Login", command=self.login)
        login_button.pack()

        register_button = tk.Button(self, text="Register", command=self.register)
        register_button.pack()

    def login(self):
        pass

    def register(self):
        pass
