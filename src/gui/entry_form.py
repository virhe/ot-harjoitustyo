import tkinter as tk
from datetime import datetime
from tkinter import Toplevel, messagebox
from tkcalendar import DateEntry


class EntryForm(Toplevel):
    def __init__(self, root, entry_service, user_id):
        super().__init__(root)
        self.entry_service = entry_service
        self.user_id = user_id
        self.title("Add Entry")
        self.geometry("400x400")

        # Fields for Entry
        tk.Label(self, text="Amount:").pack()
        self.amount = tk.Entry(self)
        self.amount.pack()

        tk.Label(self, text="Category:").pack()
        self.category = tk.Entry(self)
        self.category.pack()

        tk.Label(self, text="Date:").pack()
        self.date = DateEntry(self, date_pattern="dd-mm-yyyy")
        self.date.pack()

        tk.Label(self, text="Description:").pack()
        self.description = tk.Entry(self)
        self.description.pack()

        submit = tk.Button(self, text="Submit", command=self.submit)
        submit.pack()

    def submit(self):
        try:
            amount = float(self.amount.get())
        except ValueError:
            messagebox.showerror("Error", "Amount must be an integer.")
            return

        category = self.category.get()
        if not category:
            messagebox.showerror("Error", "Please choose a category.")
            return

        try:
            date = datetime.strptime(self.date.get(), "%d-%m-%Y").date()
        except ValueError:
            messagebox.showerror("Error", "Date must be in the DD-MM-YYYY format.")
            return

        # Optional, no validation needed
        description = self.description.get()

        try:
            self.entry_service.add_entry(
                self.user_id, amount, category, date, description)
            messagebox.showinfo("Success", "Entry added successfully")
            self.destroy()
            # pylint WOULD complain about this, but gui is omitted :)
        except Exception as e:
            messagebox.showinfo("Error", str(e))
