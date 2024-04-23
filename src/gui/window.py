import tkinter as tk

from src.gui.entry_form import EntryForm
from tkinter import ttk


class MainWindow:
    def __init__(self, root, entry_service, user_id):
        self.root = root
        self.entry_service = entry_service
        self.user_id = user_id
        self.root.title("Depysit")
        self.root.geometry("800x600")

        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Welcome to Depysit").pack()

        # Has to be instance variable for entry_form() and refresh()
        # Fills the whole window with a treeview, with buttons at the bottom
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = (
            "ID", "Amount", "Category", "Date", "Description")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("ID", anchor=tk.W, width=40)
        self.tree.column("Amount", anchor=tk.W, width=80)
        self.tree.column("Category", anchor=tk.W, width=120)
        self.tree.column("Date", anchor=tk.W, width=120)
        self.tree.column("Description", anchor=tk.W, width=200)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("ID", text="ID", anchor=tk.W)
        self.tree.heading("Amount", text="Amount", anchor=tk.W)
        self.tree.heading("Category", text="Category", anchor=tk.W)
        self.tree.heading("Date", text="Date", anchor=tk.W)
        self.tree.heading("Description", text="Description", anchor=tk.W)

        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Entry button
        add_entry = tk.Button(self.root, text="Add Entry",
                              command=self.entry_form)
        add_entry.pack()

        # Refresh button
        refresh_button = tk.Button(
            self.root, text="Refresh", command=self.refresh)
        refresh_button.pack()

        self.refresh()

    def entry_form(self):
        EntryForm(self.root, self.entry_service, self.user_id)

    def refresh(self):
        # There might be a better way?
        for entry in self.tree.get_children():
            self.tree.delete(entry)

        # Once again, there is probably a way to fill the tree without a loop
        entries = self.entry_service.entries_by_user(self.user_id)
        for entry in entries:
            self.tree.insert("", "end", values=(entry.id, entry.amount,
                                                entry.category, entry.date, entry.description))
