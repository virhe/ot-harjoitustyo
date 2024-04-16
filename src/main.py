import tkinter as tk

from src.gui.form import ComboForm
from src.repositories.entry_repository import EntryRepository
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService
from src.services.entry_service import EntryService
from src.database import init_db


def main():
    init_db()

    user_repository = UserRepository()
    entry_repository = EntryRepository()

    user_service = UserService(user_repository)
    entry_service = EntryService(entry_repository)

    root = tk.Tk()
    form = ComboForm(root, user_service)

    root.mainloop()


if __name__ == "__main__":
    main()
