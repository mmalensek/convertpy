import tkinter as tk
from logic.conversion_logic import kg_to_lbs
from logic.tkinter_logic import switch_to

def create_weight_window(parent, x=100, y=100):
    from gui.menu_window import create_menu_window

    window = tk.Toplevel()
    window.geometry(f"400x150+{x}+{y}")
    window.title("convertpy ©mmalensek")

    def convert_kg_to_lbs():
        try:
            kg = float(entry_kg.get())
            lbs = kg_to_lbs(kg)
            label_result.config(text=f"{lbs:.2f} lbs")
        except ValueError:
            label_result.config(text="Invalid input")

    # label left of the entry box
    label_kg = tk.Label(window, text="Enter weight in kg:")
    label_kg.grid(row=0, column=0, padx=5, pady=10)

    # entry box
    entry_kg = tk.Entry(window)
    entry_kg.grid(row=0, column=1, padx=5, pady=0)

    # result label
    label_result = tk.Label(window, text="")
    label_result.grid(row=0, column=2, padx=5, pady=5)

    # return to menu_window
    button_return = tk.Button(window, text="return", command=lambda: switch_to(window, create_menu_window))
    button_return.grid(row=1, column=0, pady=0)

    # convert button
    button_convert = tk.Button(window, text="convert", command=convert_kg_to_lbs)
    button_convert.grid(row=1, column=1, pady=0)

    return window
