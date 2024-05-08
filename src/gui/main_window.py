import tkinter as tk
from collections import defaultdict
from tkinter import ttk

import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from src.gui.entry_form import EntryForm


class MainWindow:
    """Represents the application main window"""

    # MAIN SECTION
    def __init__(self, root, entry_service, user_id):
        """Constructor

        Args:
            root: tkinter root
            entry_service: entry_service instance
            user_id: user_id of the current user
        """

        self.root = root
        self.entry_service = entry_service
        self.user_id = user_id
        self.root.title("Depysit")
        self.root.geometry("1000x800")

        self.create_ui()

    def create_ui(self):
        """Creates the main ui elements"""

        notebook = ttk.Notebook(self.root)
        entry_tab = ttk.Frame(notebook)
        graph_tab = ttk.Frame(notebook)
        notebook.add(entry_tab, text="Entries")
        notebook.add(graph_tab, text="Graph")
        notebook.pack(fill="both", expand=True)

        self.create_entries_tab(entry_tab)
        self.create_graph_tab(graph_tab)

    # -----

    # ENTRY SECTION
    def create_entries_tab(self, entry_tab):
        """Creates the entries tab

        Args:
            entry_tab: tkinter Frame
        """

        # Has to be instance variable for entry_form() and refresh()
        # Fills the whole window with a treeview, with buttons at the bottom
        self.tree = ttk.Treeview(entry_tab)
        self.tree["columns"] = (
            "ID",
            "Type",
            "Amount",
            "Category",
            "Date",
            "Description",
        )
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("ID", anchor=tk.W, width=40)
        self.tree.column("Type", anchor=tk.W, width=80)
        self.tree.column("Amount", anchor=tk.W, width=80)
        self.tree.column("Category", anchor=tk.W, width=120)
        self.tree.column("Date", anchor=tk.W, width=120)
        self.tree.column("Description", anchor=tk.W, width=200)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("ID", text="ID", anchor=tk.W)
        self.tree.heading("Type", text="Type", anchor=tk.W)
        self.tree.heading("Amount", text="Amount", anchor=tk.W)
        self.tree.heading("Category", text="Category", anchor=tk.W)
        self.tree.heading("Date", text="Date", anchor=tk.W)
        self.tree.heading("Description", text="Description", anchor=tk.W)

        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add Entry button
        add_entry = tk.Button(entry_tab, text="Add Entry", command=self.entry_form)
        add_entry.pack()

        # Delete Entry button
        delete_entry = tk.Button(
            entry_tab, text="Delete Entry", command=self.delete_entry
        )
        delete_entry.pack()

        self.refresh()

    def entry_form(self):
        """Shows EntryForm when "Add Entry" is clicked"""

        EntryForm(
            self.root, self.entry_service, self.user_id, on_entry_add=self.on_entry_add
        )

    def delete_entry(self):
        """Deletes selected entry from the TreeView"""

        entry = self.tree.selection()
        if entry:
            entry_id = self.tree.item(entry)["values"][0]
            self.tree.delete(entry)
            self.entry_service.delete_entry(entry_id)
            self.refresh()

    def on_entry_add(self):
        """Updates TreeView and graph when entry is successfully added"""

        self.refresh()
        self.update_years()

    def refresh(self):
        """Updates TreeView"""

        # There might be a better way?
        for entry in self.tree.get_children():
            self.tree.delete(entry)

        # Once again, there is probably a way to fill the tree without a loop
        entries = self.entry_service.entries_by_user(self.user_id)
        for entry in entries:
            self.tree.insert(
                "",
                "end",
                values=(
                    entry.id,
                    entry.type,
                    entry.amount,
                    entry.category,
                    entry.date,
                    entry.description,
                ),
            )

    # -----

    # GRAPH SECTION
    def create_graph_tab(self, graph_tab):
        """Creates the graph tab

        Args:
            graph_tab: tkinter Frame
        """

        self.figure = Figure(figsize=(10, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, graph_tab)
        self.canvas.get_tk_widget().pack()

        tk.Label(graph_tab, text="Year:").pack()
        self.years = ttk.Combobox(graph_tab, values=self.entry_years())
        self.years.pack()

        if self.years["values"]:
            self.years.set(self.years["values"][0])

        tk.Label(graph_tab, text="Month:").pack()
        self.months = ttk.Combobox(
            graph_tab,
            values=[
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ],
        )
        self.months.pack()

        if self.months["values"]:
            self.months.set(self.months["values"][0])

        update_button = tk.Button(graph_tab, text="Update", command=self.update_graph)
        update_button.pack()

    def plot_graph(self, entries):
        """Plots the data on the graph

        Args:
            entries: list of entries to graph
        """

        # ChatGPT generated line, had trouble with this.
        entries_on_date = defaultdict(lambda: {"income": 0, "expense": 0})

        for entry in entries:
            if entry.type == "Income":
                entries_on_date[entry.date]["income"] += entry.amount
            else:
                entries_on_date[entry.date]["expense"] += entry.amount

        sorted_dates = sorted(entries_on_date.keys())
        net = [
            entries_on_date[date]["income"] - entries_on_date[date]["expense"]
            for date in sorted_dates
        ]

        self.ax.clear()
        self.ax.set_title("Net Finances on Given Month")
        self.ax.set_xlabel("Day")
        self.ax.set_ylabel("Amount")

        color = ["green" if x >= 0 else "red" for x in net]
        bars = self.ax.bar(sorted_dates, net, color=color)

        self.ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter("%d"))
        self.figure.autofmt_xdate()

        for bar in bars:
            val = bar.get_height()

            if val >= 0:
                v_align = "top"
            else:
                v_align = "bottom"

            self.ax.text(
                bar.get_x() + bar.get_width() / 2,
                val,
                "%d" % val,
                ha="center",
                va=v_align,
                rotation="vertical",
            )

        self.canvas.draw()

    def entry_years(self):
        """Returns all years with entries

        Returns:
            years: list of years
        """

        entries = self.entry_service.entries_by_user(self.user_id)
        years = sorted({entry.date.year for entry in entries})
        return years

    def update_years(self):
        """Updates the year combobox"""

        years = self.entry_years()
        self.years["values"] = years

        if years:
            self.years.set(years[0])
        else:
            self.years.set("")

    def update_graph(self):
        """Updates the graph"""

        year = int(self.years.get())
        month = self.months.current() + 1

        if not year:
            return

        entries = self.entry_service.entries_by_user(self.user_id)
        entries_on_date = [
            entry
            for entry in entries
            if entry.date.year == year and entry.date.month == month
        ]

        self.plot_graph(entries_on_date)

    # -----
