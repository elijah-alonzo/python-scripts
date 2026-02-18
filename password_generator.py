import random
import string
import tkinter as tk
from tkinter import messagebox, ttk

def generate_password(length=16, use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation if use_symbols else ""

    all_chars = letters + digits + symbols

    password = "".join(random.choice(all_chars) for _ in range(length))
    return password


class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("320x180")
        self.root.resizable(False, False)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        frame = ttk.Frame(self.root, padding=14)
        frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(frame, text="Length:").grid(row=0, column=0, sticky="w", pady=(0, 8))
        self.length_var = tk.StringVar(value="16")
        ttk.Entry(frame, textvariable=self.length_var).grid(row=0, column=1, sticky="ew", pady=(0, 8))

        self.symbols_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(frame, text="Include symbols", variable=self.symbols_var).grid(
            row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10)
        )

        ttk.Button(frame, text="Generate Password", command=self.on_generate).grid(
            row=2, column=0, columnspan=2, sticky="ew", pady=(0, 10)
        )

        ttk.Label(frame, text="Generated password:").grid(row=3, column=0, columnspan=2, sticky="w")
        self.password_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.password_var, state="readonly").grid(
            row=4, column=0, columnspan=2, sticky="ew", pady=(4, 0)
        )

        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(1, weight=1)

    def on_generate(self):
        try:
            length = int(self.length_var.get().strip() or "0")
        except ValueError:
            messagebox.showerror("Invalid length", "Please enter a valid whole number.")
            return

        if length <= 0:
            messagebox.showerror("Invalid length", "Length must be greater than 0.")
            return

        password = generate_password(length=length, use_symbols=self.symbols_var.get())
        self.password_var.set(password)


def main():
    root = tk.Tk()
    PasswordGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
