import tkinter as tk
from datetime import datetime
from tkinter import Toplevel, messagebox


class EntryForm(Toplevel):
    def __init__(self, root, entry_service, user_id):
        super().__init__(root)
        self.entry_service = entry_service
        self.user_id = user_id
        self.title("Add Entry")
        self.geometry("400x400")

        tk.Label(self, text="Amount:").pack()
        self.amount = tk.Entry(self)
        self.amount.pack()

        tk.Label(self, text="Category:").pack()
        self.category = tk.Entry(self)
        self.category.pack()

        tk.Label(self, text="Date (DD-MM-YYYY):").pack()
        self.date = tk.Entry(self)
        self.date.pack()

        tk.Label(self, text="Description:").pack()
        self.description = tk.Entry(self)
        self.description.pack()

        submit = tk.Button(self, text="Submit", command=self.submit)
        submit.pack()

    def submit(self):
        try:
            amount = float(self.amount.get())
            category = self.category.get()
            date = datetime.strptime(self.date.get(), "%d-%m-%Y").date()
            description = self.description.get()

            self.entry_service.add_entry(
                self.user_id, amount, category, date, description)
            messagebox.showinfo("Success", "Entry added successfully")
            self.destroy()
        except Exception as e:
            messagebox.showinfo("Error", str(e))
