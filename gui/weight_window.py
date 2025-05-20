import tkinter as tk
from logic.conversion_logic import kg_to_lbs
from logic.tkinter_logic import switch_to

def create_weight_window(x=100, y=100):
    from gui.menu_window import create_menu_window

    root = tk.Tk()
    root.geometry(f"400x150+{x}+{y}")
    root.title("convertpy ©mmalensek")

    def convert_kg_to_lbs():
        try:
            kg = float(entry_kg.get())
            lbs = kg_to_lbs(kg)
            label_result.config(text=f"{lbs:.2f} lbs")
        except ValueError:
            label_result.config(text="Invalid input")

    # label left of the entry box
    label_kg = tk.Label(root, text="Enter weight in kg:")
    label_kg.grid(row=0, column=0, padx=5, pady=10)

    # entry box
    entry_kg = tk.Entry(root)
    entry_kg.grid(row=0, column=1, padx=5, pady=0)

    # result label
    label_result = tk.Label(root, text="")
    label_result.grid(row=0, column=2, padx=5, pady=5)

    # return to menu_window
    button_return = tk.Button(root, text="Return", command=lambda: switch_to(root, create_menu_window))
    button_return.grid(row=1, column=0, pady=0)

    # convert button
    button_convert = tk.Button(root, text="convert", command=convert_kg_to_lbs)
    button_convert.grid(row=1, column=1, pady=0)

    root.mainloop()
