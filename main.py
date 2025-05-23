import tkinter as tk
from tkinter import ttk
import pyperclip
import random
import string

def generate_password():
    length = int(entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    label_result.config(text=password)

def copy_to_clipboard():
    password = label_result.cget("text")
    pyperclip.copy(password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")
root.configure(bg="#132054")
root.iconbitmap("img/icon.ico")

style = ttk.Style()
style.configure("TButton", padding=5, font=("Arial", 10))

ttk.Label(root, text="Password Length:", foreground="white", background="#2C3E50").pack(pady=5)

entry = ttk.Entry(root)
entry.pack()

ttk.Button(root, text="Generate", command=generate_password).pack(pady=5)
ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

label_result = ttk.Label(root, text="", font=("Arial", 12), foreground="white", background="#2C3E50")
label_result.pack(pady=10)

root.mainloop()