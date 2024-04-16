import tkinter as tk

from src.gui.entry_form import EntryForm


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

        add_entry = tk.Button(self.root, text="Add Entry", command=self.entry_form)
        add_entry.pack()


    def entry_form(self):
        entry_form = EntryForm(self.root, self.entry_service, self.user_id)