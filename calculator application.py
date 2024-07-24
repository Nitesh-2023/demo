'''calculator application that perform basic operation'''
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation.get() == "Addition":
            result = num1 + num2
        elif operation.get() == "Subtraction":
            result = num1 - num2
        elif operation.get() == "Multiplication":
            result = num1 * num2
        elif operation.get() == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        messagebox.showinfo("Result", f"The result is: {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the main window
app = tk.Tk()
app.title("Simple Calculator")

# Create and place widgets
label_num1 = tk.Label(app, text="Enter number 1:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(app)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(app, text="Enter number 2:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(app)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_operation = tk.Label(app, text="Select operation:")
label_operation.grid(row=2, column=0, padx=10, pady=10)

operation = tk.StringVar()
operation.set("Addition")

operation_menu = tk.OptionMenu(app, operation, "Addition", "Subtraction", "Multiplication", "Division")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(app, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main loop
app.mainloop()