import tkinter as tk

# --- Functions ---
def press(value):
    global expression
    expression += str(value)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("0")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# --- Main Window ---
root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")
root.geometry("320x500")
root.resizable(False, False)

expression = ""
equation = tk.StringVar()
equation.set("0")

# --- Display ---
display = tk.Label(
    root,
    textvariable=equation,
    font=("Helvetica", 40),
    bg="black",
    fg="white",
    anchor="e",
    padx=20
)
display.pack(expand=True, fill="both")

# --- Button Frame ---
frame = tk.Frame(root, bg="black")
frame.pack(expand=True, fill="both")

# Button styles
btn_bg_dark = "#333333"
btn_bg_light = "#A5A5A5"
btn_bg_orange = "#FF9500"

buttons = [
    [("AC", btn_bg_light), ("+/-", btn_bg_light), ("%", btn_bg_light), ("/", btn_bg_orange)],
    [("7", btn_bg_dark), ("8", btn_bg_dark), ("9", btn_bg_dark), ("*", btn_bg_orange)],
    [("4", btn_bg_dark), ("5", btn_bg_dark), ("6", btn_bg_dark), ("-", btn_bg_orange)],
    [("1", btn_bg_dark), ("2", btn_bg_dark), ("3", btn_bg_dark), ("+", btn_bg_orange)],
    [("0", btn_bg_dark), (".", btn_bg_dark), ("=", btn_bg_orange)]
]

for row in buttons:
    row_frame = tk.Frame(frame, bg="black")
    row_frame.pack(expand=True, fill="both")
    
    for (text, color) in row:
        if text == "0":
            btn = tk.Button(
                row_frame,
                text=text,
                font=("Helvetica", 20),
                bg=color,
                fg="white",
                bd=0,
                command=lambda t=text: press(t)
            )
            btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        else:
            btn = tk.Button(
                row_frame,
                text=text,
                font=("Helvetica", 20),
                bg=color,
                fg="white",
                bd=0,
                command=lambda t=text: (
                    clear() if t == "AC" else
                    calculate() if t == "=" else
                    press(t)
                )
            )
            btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

root.mainloop()
