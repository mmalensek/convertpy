import tkinter as tk
from logic.conversion_logic import kg_to_lbs

def create_weight_window(x=100, y=100):
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

    # Label on row 0, column 0
    label_kg = tk.Label(root, text="Enter weight in kg:")
    label_kg.grid(row=0, column=0, padx=5, pady=10)

    # Entry on row 0, column 1
    entry_kg = tk.Entry(root)
    entry_kg.grid(row=0, column=1, padx=5, pady=0)

    # Result label on row 0, column 2 (right of the entry field)
    label_result = tk.Label(root, text="")
    label_result.grid(row=0, column=2, padx=5, pady=5)

    # Convert button on row 1, centered
    button_convert = tk.Button(root, text="convert", command=convert_kg_to_lbs)
    button_convert.grid(row=1, column=1, pady=0)

    root.mainloop()
