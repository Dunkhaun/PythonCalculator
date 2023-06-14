import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero!"
        else:
            result = "Invalid operator"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="Result: ")

def add_decimal():
    current_entry = window.focus_get()
    current_entry.insert(tk.END, ".")

def change_theme(theme_name):
    window.style.theme_use(theme_name)
    # Reapply the font size
    change_font_size(font_size_combobox.get())

def change_font_size(size):
    window.style.configure("TLabel", font=("TkDefaultFont", size))
    window.style.configure("TButton", font=("TkDefaultFont", size))
    window.style.configure("TEntry", font=("TkDefaultFont", size))
    window.style.configure("TMenubutton", font=("TkDefaultFont", size))
    window.style.configure("TCombobox", font=("TkDefaultFont", size))

def bind_keyboard(event):
    key = event.keysym.lower()
    if key == "return":
        calculate()
    elif key == "escape":
        clear()
    elif key == ".":
        add_decimal()

def main():
    global entry_num1, entry_num2, operator_var, result_label, window

    window = tk.Tk()
    window.title("Calculator")
    window.style = ttk.Style()

    # Theme selection
    themes = [
        "default",
        "clam",
        "alt",
        "classic",
        "vista",
        "xpnative"
    ]

    theme_label = ttk.Label(window, text="Select Theme:")
    theme_label.pack()

    theme_combobox = ttk.Combobox(window, values=themes, state="readonly")
    theme_combobox.current(0)
    theme_combobox.pack()

    theme_button = ttk.Button(window, text="Apply Theme", command=lambda: change_theme(theme_combobox.get()))
    theme_button.pack()

    # Font size selection
    font_sizes = [8, 10, 12, 14, 16, 18]

    font_size_label = ttk.Label(window, text="Select Font Size:")
    font_size_label.pack()

    font_size_combobox = ttk.Combobox(window, values=font_sizes, state="readonly")
    font_size_combobox.current(2)  # Default font size
    font_size_combobox.pack()

    font_size_button = ttk.Button(window, text="Apply Font Size", command=lambda: change_font_size(font_size_combobox.get()))
    font_size_button.pack()

    # Calculator GUI
    num1_label = ttk.Label(window, text="Number 1:")
    num1_label.pack()

    entry_num1 = ttk.Entry(window)
    entry_num1.pack()

    num2_label = ttk.Label(window, text="Number 2:")
    num2_label.pack()

    entry_num2 = ttk.Entry(window)
    entry_num2.pack()

    operator_label = ttk.Label(window, text="Operator:")
    operator_label.pack()

    operator_var = tk.StringVar()
    operator_var.set("+")

    operator_options = ["+", "-", "*", "/"]

    operator_menu = ttk.OptionMenu(window, operator_var, *operator_options)
    operator_menu.pack()

    calculate_button = ttk.Button(window, text="Calculate", command=calculate)
    calculate_button.pack()

    result_label = ttk.Label(window, text="Result: ")
    result_label.pack()

    clear_button = ttk.Button(window, text="Clear", command=clear)
    clear_button.pack()

    window.bind("<Key>", bind_keyboard)
    window.mainloop()

if __name__ == "__main__":
    main()
