import tkinter as tk

# get coordinates to center a window
def get_center_coordinates(width=450, height=150):
    temp = tk.Tk()
    temp.withdraw()
    screen_width = temp.winfo_screenwidth()
    screen_height = temp.winfo_screenheight()
    temp.destroy()
    return (screen_width // 2) - (width // 2), (screen_height // 2) - (height // 2)

def switch_to(current_window, next_window_fn):
    # save coordinates of previous window
    x = current_window.winfo_x()
    y = current_window.winfo_y()

    current_window.destroy()
    next_window_fn(x, y)
