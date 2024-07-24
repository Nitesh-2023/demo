import tkinter as tk
from tkinter import messagebox

def on_submit():
    try:
        print("jnjnj")
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        messagebox.showinfo("Result", f"The sum is: {result}")
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

submit_button = tk.Button(app, text="Submit", command=on_submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the main loop
app.mainloop()
