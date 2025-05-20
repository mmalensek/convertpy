import tkinter as tk
from gui.menu_window import create_menu_window

if __name__ == "__main__":
    # run root (bottom) window
    root = tk.Tk()
    root.withdraw()

    # run main menu window
    create_menu_window(root)

    # run until closed, for user input
    root.mainloop()
