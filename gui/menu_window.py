import tkinter as tk
from logic.tkinter_logic import get_center_coordinates, switch_to

def create_menu_window(parent, x=-1, y=-1):
    from gui.weight_window import create_weight_window

    window = tk.Toplevel(parent)
    window.title("convertpy ©mmalensek")

    # set window size
    width = 400
    height = 150

    # get x and y coordinates to open the window on center of the screen
    if(x == -1 and y == -1):
        x, y = get_center_coordinates(width, height)

    window.geometry(f"{width}x{height}+{x}+{y}")

    label = tk.Label(window, text="What do you want to convert?")
    label.pack(pady=10)

    button_kg = tk.Button(window, text="kg -> lbs", command=lambda: switch_to(window, create_weight_window))
    button_kg.pack(pady=5)

    # TO-DO
    # new conversion windows / logic

    return window
