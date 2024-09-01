import tkinter as tk

# Function to update the display
def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")  # Adjust size as needed
root.resizable(False, False)

# Display frame
display_frame = tk.Frame(root)
display_frame.pack(pady=20)

# Calculator display (Entry widget)
display = tk.Entry(display_frame, font=("Arial", 24), borderwidth=5, relief="sunken", justify="right")
display.pack(padx=10, pady=10, fill="both")

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button configuration
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add buttons to the grid
for (text, row, col) in buttons:
    button = tk.Button(button_frame, text=text, font=("Arial", 18),padx=20, pady=20, 
                       command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Add a clear button
clear_button = tk.Button(button_frame, text="C", font=("Arial", 18), padx=20, pady=20, 
                         command=clear_display)
clear_button.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

# Adjust rows and columns weights to make the buttons expand equally
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# Attach the equals button functionality
equals_button = tk.Button(button_frame, text="=", font=("Arial", 18), padx=20, pady=20, 
                          command=evaluate_expression)
equals_button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

# Start the Tkinter loop
root.mainloop()