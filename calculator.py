import tkinter as tk

# Function to update the expression in the entry field
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the entry box
    entry.insert(tk.END, current + str(value))  # Append the value to current expression

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())  # Using eval to evaluate the string expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")  # Size of the window

# Create an entry field to show the current expression
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout in a grid format
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 20), command=evaluate)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 20), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 20), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Start the main event loop
root.mainloop()
