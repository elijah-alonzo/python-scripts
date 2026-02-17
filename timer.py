import tkinter as tk
from tkinter import messagebox

# --- Functions ---
def start_timer():
    global running
    if not running:
        try:
            total_seconds = int(min_entry.get()) * 60 + int(sec_entry.get())
            if total_seconds <= 0:
                messagebox.showwarning("Invalid Time", "Enter a positive time.")
                return
            running = True
            countdown(total_seconds)
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter numbers only.")

def countdown(seconds):
    global running
    if seconds >= 0 and running:
        mins = seconds // 60
        secs = seconds % 60
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        root.after(1000, countdown, seconds - 1)
    else:
        if running:
            messagebox.showinfo("Time's Up!", "⏰ Timer finished!")
            running = False

def pause_timer():
    global running
    running = False

def reset_timer():
    global running
    running = False
    timer_label.config(text="00:00")
    min_entry.delete(0, tk.END)
    sec_entry.delete(0, tk.END)

# --- Main Window ---
root = tk.Tk()
root.title("iOS-Style Timer")
root.geometry("350x300")
root.configure(bg="#f0f0f5")
root.resizable(False, False)

running = False

# --- Header ---
header = tk.Label(root, text="⏱ Timer", font=("Helvetica", 24, "bold"), bg="#f0f0f5")
header.pack(pady=10)

# --- Timer Display ---
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48, "bold"), bg="#f0f0f5")
timer_label.pack(pady=10)

# --- Time Input ---
input_frame = tk.Frame(root, bg="#f0f0f5")
input_frame.pack(pady=10)

min_entry = tk.Entry(input_frame, font=("Helvetica", 16), width=3, justify="center", bd=1, relief=tk.RIDGE)
min_entry.pack(side=tk.LEFT, padx=5)
tk.Label(input_frame, text=":", font=("Helvetica", 16), bg="#f0f0f5").pack(side=tk.LEFT)
sec_entry = tk.Entry(input_frame, font=("Helvetica", 16), width=3, justify="center", bd=1, relief=tk.RIDGE)
sec_entry.pack(side=tk.LEFT, padx=5)

# --- Buttons ---
button_frame = tk.Frame(root, bg="#f0f0f5")
button_frame.pack(pady=20)

start_btn = tk.Button(button_frame, text="Start", font=("Helvetica", 14), bg="#007AFF", fg="white",
                      bd=0, relief=tk.FLAT, padx=15, command=start_timer)
start_btn.pack(side=tk.LEFT, padx=5)

pause_btn = tk.Button(button_frame, text="Pause", font=("Helvetica", 14), bg="#34C759", fg="white",
                      bd=0, relief=tk.FLAT, padx=15, command=pause_timer)
pause_btn.pack(side=tk.LEFT, padx=5)

reset_btn = tk.Button(button_frame, text="Reset", font=("Helvetica", 14), bg="#FF3B30", fg="white",
                      bd=0, relief=tk.FLAT, padx=15, command=reset_timer)
reset_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()
