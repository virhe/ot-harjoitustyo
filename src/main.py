import tkinter as tk
import os
import sys

# ChatGPT generated, had issues with the terminal after developing in PyCharm.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=wrong-import-position
# Hopefully a reasonable reason to disable the warning in this case

from src.gui.form import ComboForm
from src.gui.window import MainWindow
from src.repositories.entry_repository import EntryRepository
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService
from src.services.entry_service import EntryService
from src.database import init_db, session


def main():
    init_db()

    user_repository = UserRepository(session)
    entry_repository = EntryRepository(session)

    user_service = UserService(user_repository)
    entry_service = EntryService(entry_repository)

    root = tk.Tk()
    # Hide main window
    root.withdraw()

    # On successful login or register
    def success(user_id):
        # Show main window
        root.deiconify()
        MainWindow(root, entry_service, user_id)
        root.mainloop()

    form = ComboForm(root, user_service, success)
    form.mainloop()


if __name__ == "__main__":
    main()
