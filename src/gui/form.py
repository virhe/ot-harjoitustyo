import tkinter as tk
from tkinter import Toplevel, messagebox


class ComboForm(Toplevel):
    def __init__(self, root, user_service):
        super().__init__(root)
        self.user_service = user_service
        self.title("Login/Register")
        self.geometry("300x300")

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
        username = self.username.get()
        password = self.password.get()

        if self.user_service.login(username, password):
            messagebox.showinfo("Login Successful", "You are now logged in.")
            self.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password.")

    def register(self):
        username = self.username.get()
        password = self.password.get()

        try:
            self.user_service.register(username, password)
            messagebox.showinfo("Registration Successful", "You are now registered.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Registration Failed", str(e))
