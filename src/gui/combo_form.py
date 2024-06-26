import tkinter as tk

from tkinter import Toplevel, messagebox


class ComboForm(Toplevel):
    """Represents a login/register form."""

    def __init__(self, root, user_service, success):
        """Constructor

        Args:
            root: tkinter root
            user_service: user_service instance
            success: bool, true if user was successfully logged in / registered
        """

        super().__init__(root)
        self.user_service = user_service
        self.title("Login/Register")
        self.geometry("300x300")

        self.success = success

        # Shared fields for login and register
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
        """Responsible for logging a user in"""

        username = self.username.get()
        password = self.password.get()

        user_id = self.user_service.login(username, password)

        if user_id:
            messagebox.showinfo("Login Successful", "You are now logged in.")
            self.destroy()
            self.success(user_id)
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password.")

    def register(self):
        """Responsible for registering a user

        Raises:
            Exception, if user is not successfully registered
        """

        username = self.username.get()
        password = self.password.get()

        try:
            # Try registering new user
            user_id = self.user_service.register(username, password)
            if user_id:
                messagebox.showinfo(
                    "Registration Successful", "You are now registered."
                )
                self.destroy()
                self.success(user_id)
        # Broad exception, but pylint omitted file
        except Exception as e:
            messagebox.showerror("Registration Failed", str(e))
