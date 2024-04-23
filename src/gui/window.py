import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
        notebook = ttk.Notebook(self.root)
        entry_tab = ttk.Frame(notebook)
        graph_tab = ttk.Frame(notebook)
        notebook.add(entry_tab, text="Entries")
        notebook.add(graph_tab, text="Graph")
        notebook.pack(fill="both", expand=True)

        self.create_entries_tab(entry_tab)
        self.create_graph_tab(graph_tab)

    def create_entries_tab(self, entry_tab):
        # Has to be instance variable for entry_form() and refresh()
        # Fills the whole window with a treeview, with buttons at the bottom
        self.tree = ttk.Treeview(entry_tab)
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
        add_entry = tk.Button(entry_tab, text="Add Entry",
                              command=self.entry_form)
        add_entry.pack()

        # Refresh button
        refresh_button = tk.Button(
            entry_tab, text="Refresh", command=self.refresh)
        refresh_button.pack()

        self.refresh()

    def create_graph_tab(self, graph_tab):
        figure = Figure(figsize=(6, 6), dpi=100)
        canvas = FigureCanvasTkAgg(figure, graph_tab)
        canvas.get_tk_widget().pack()

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
