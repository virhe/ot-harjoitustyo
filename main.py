import tkinter as tk

from src.database import init_db, session
from src.gui.combo_form import ComboForm
from src.gui.main_window import MainWindow
from src.repositories.entry_repository import EntryRepository
from src.repositories.user_repository import UserRepository
from src.services.entry_service import EntryService
from src.services.user_service import UserService


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
