import tkinter as tk

# Function to evaluate the expression and update the display
def evaluate_expression():
    try:
        result = str(eval(display.get()))
        display.set(result)
    except:
        display.set("Error")

# Function to update the display with the pressed key
def update_display(key):
    if display.get() == "Error":
        display.set("")
    display.set(display.get() + key)

# Function to clear the display
def clear_display():
    display.set("")

# Function to clear the last digit
def clear_last_digit():
    current_text = display.get()
    display.set(current_text[:-1])

# Setting up the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='#2E2E2E')
root.resizable(0, 0)

display = tk.StringVar()

# Entry widget for the display
entry = tk.Entry(root, textvariable=display, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4, bg='#D9E4EC', fg='#000000')
entry.grid(row=0, column=0, columnspan=4)

# List of button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Creating and placing buttons on the grid
row, col = 1, 0
for button in buttons:
    action = lambda x=button: update_display(x) if x != "=" else evaluate_expression()
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=action, bg='#4F5A69', fg='#FFFFFF', activebackground='#89A4C0', activeforeground='#FFFFFF').grid(row=row, column=col, sticky='nsew')
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear all button
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=clear_display, bg='#E25757', fg='#FFFFFF', activebackground='#F28B82', activeforeground='#FFFFFF').grid(row=row, column=col, sticky='nsew')
col += 1

# Clear last digit button
tk.Button(root, text='←', padx=20, pady=20, font=('Arial', 18), command=clear_last_digit, bg='#E25757', fg='#FFFFFF', activebackground='#F28B82', activeforeground='#FFFFFF').grid(row=row, column=col, sticky='nsew')

# Make buttons fill the space
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Running the application
root.mainloop()