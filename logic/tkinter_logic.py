import tkinter as tk

# get coordinates to center a window
def get_center_coordinates(width=450, height=150):
    temp = tk.Tk()
    temp.withdraw()
    screen_width = temp.winfo_screenwidth()
    screen_height = temp.winfo_screenheight()
    temp.destroy()
    return (screen_width // 2) - (width // 2), (screen_height // 2) - (height // 2)
