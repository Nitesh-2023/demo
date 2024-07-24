'''password generator application that generate random password on user given length'''
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_password():
    length = int(entry_length.get())
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    generated_password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)

    if generated_password:
        result_label.config(text=f"Generated Password: {generated_password}")

# Create the main window
app = tk.Tk()
app.title("Password Generator")

# Create and place widgets
label_length = tk.Label(app, text="Password Length:")
label_length.grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(app)
entry_length.grid(row=0, column=1, padx=10, pady=10)

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_chars_var = tk.BooleanVar()

uppercase_checkbox = tk.Checkbutton(app, text="Uppercase", variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=0, padx=10, pady=5)

lowercase_checkbox = tk.Checkbutton(app, text="Lowercase", variable=lowercase_var)
lowercase_checkbox.grid(row=1, column=1, padx=10, pady=5)

digits_checkbox = tk.Checkbutton(app, text="Digits", variable=digits_var)
digits_checkbox.grid(row=2, column=0, padx=10, pady=5)

special_chars_checkbox = tk.Checkbutton(app, text="Special Characters", variable=special_chars_var)
special_chars_checkbox.grid(row=2, column=1, padx=10, pady=5)

generate_button = tk.Button(app, text="Generate Password", command=on_generate_password)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(app, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main loop
app.mainloop()