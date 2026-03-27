import tkinter as tk
from tkinter import ttk
import re

def check_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[@#$%^&+=!]", password):
        score += 1

    return score

def analyze():
    pwd = entry.get()
    score = check_strength(pwd)

    progress['value'] = score * 25

    if score == 4:
        result_label.config(text="Strong ", fg="green")
    elif score == 3:
        result_label.config(text="Medium ⚠️", fg="orange")
    else:
        result_label.config(text="Weak ❌", fg="red")

# UI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x350")
root.configure(bg="#1e293b")

title = tk.Label(root, text="Password Checker", font=("Arial", 16, "bold"),
                 fg="white", bg="#1e293b")
title.pack(pady=15)

entry = tk.Entry(root, show="*", font=("Arial", 14), width=25)
entry.pack(pady=10)

btn = tk.Button(root, text="Analyze", command=analyze,
                bg="#22c55e", fg="white", font=("Arial", 12, "bold"))
btn.pack(pady=10)

progress = ttk.Progressbar(root, length=250, maximum=100)
progress.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"),
                        bg="#1e293b")
result_label.pack(pady=10)

root.mainloop()
