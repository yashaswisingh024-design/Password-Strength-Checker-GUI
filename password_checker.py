import tkinter as tk
from tkinter import ttk
import string

def calculate_strength(password):
    length = len(password) >= 8
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    score = sum([length, upper, lower, digit, special])
    return score

def update_strength(event=None):
    pwd = entry.get()
    score = calculate_strength(pwd)

    # Update progress bar
    progress['value'] = score * 20

    # Strength text + color
    if score <= 2:
        result_label.config(text="Weak ❌", foreground="red")
    elif score <= 4:
        result_label.config(text="Medium ⚠️", foreground="orange")
    else:
        result_label.config(text="Strong ✅", foreground="green")

def toggle_password():
    if show_var.get():
        entry.config(show="")
    else:
        entry.config(show="*")

# Window
root = tk.Tk()
root.title("Password Strength Checker 🔐")
root.geometry("420x350")
root.resizable(False, False)

# Title
ttk.Label(root, text="🔐 Password Strength Checker", 
          font=("Segoe UI", 14, "bold")).pack(pady=10)

# Entry
entry = ttk.Entry(root, width=30, show="*")
entry.pack(pady=10)

# Real-time checking
entry.bind("<KeyRelease>", update_strength)

# Show/Hide checkbox
show_var = tk.BooleanVar()
ttk.Checkbutton(root, text="Show Password 👁️", 
                variable=show_var, command=toggle_password).pack()

# Progress bar
progress = ttk.Progressbar(root, length=250, maximum=100)
progress.pack(pady=15)

# Result label
result_label = ttk.Label(root, text="", font=("Segoe UI", 12, "bold"))
result_label.pack(pady=5)

# Run
root.mainloop()