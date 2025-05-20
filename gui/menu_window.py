import tkinter as tk
from gui.weight_window import create_weight_window
from logic.tkinter_logic import get_center_coordinates

def open_menu():
    root = tk.Tk()
    root.title("convertpy ©mmalensek")

    # set window size
    width = 400
    height = 150

    # get x and y coordinates to open the window on center of the screen
    x, y = get_center_coordinates(width, height)

    root.geometry(f"{width}x{height}+{x}+{y}")

    label = tk.Label(root, text="What do you want to convert?")
    label.pack(pady=10)

    button_kg = tk.Button(root, text="Kilograms → Pounds", command=lambda: switch_to(root, create_weight_window))
    button_kg.pack(pady=5)

    # TO-DO
    # new conversion windows / logic

    root.mainloop()

def switch_to(current_window, next_window_fn):
    # save coordinates of previous window
    x = current_window.winfo_x()
    y = current_window.winfo_y()

    current_window.destroy()
    next_window_fn(x, y)
