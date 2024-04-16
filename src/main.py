import tkinter as tk

from src.gui.window import MainWindow
from src.services.user_service import UserService


def main():
    root = tk.Tk()

    user_service = UserService()

    app = MainWindow(root, user_service)

    root.mainloop()


if __name__ == "__main__":
    main()
