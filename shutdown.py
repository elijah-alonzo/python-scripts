import subprocess
import sys
import tkinter as tk
from tkinter import messagebox, ttk

def shutdown_pc():
    """Trigger an immediate OS shutdown command."""
    if sys.platform == "win32":
        command = ["shutdown", "/s", "/t", "0"]
    else:  # Linux/Mac
        command = ["shutdown", "-h", "now"]

    subprocess.run(command, check=True)


class ShutdownGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Schedule Shutdown")
        self.root.resizable(False, False)

        self.timer_id = None
        self.remaining_seconds = 0

        frame = ttk.Frame(self.root, padding=14)
        frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(frame, text="Hours:").grid(row=0, column=0, sticky="w", pady=(0, 6))
        self.hour_var = tk.StringVar(value="0")
        ttk.Entry(frame, textvariable=self.hour_var).grid(row=0, column=1, sticky="ew", pady=(0, 6))

        ttk.Label(frame, text="Minutes:").grid(row=1, column=0, sticky="w", pady=(0, 6))
        self.minute_var = tk.StringVar(value="0")
        ttk.Entry(frame, textvariable=self.minute_var).grid(row=1, column=1, sticky="ew", pady=(0, 6))

        ttk.Label(frame, text="Seconds:").grid(row=2, column=0, sticky="w", pady=(0, 6))
        self.second_var = tk.StringVar(value="0")
        ttk.Entry(frame, textvariable=self.second_var).grid(row=2, column=1, sticky="ew", pady=(0, 6))

        buttons = ttk.Frame(frame)
        buttons.grid(row=3, column=0, columnspan=2, pady=(4, 8), sticky="ew")

        ttk.Button(buttons, text="Schedule Shutdown", command=self.schedule_shutdown).grid(row=0, column=0, padx=(0, 6))
        ttk.Button(buttons, text="Shutdown Now", command=self.shutdown_now).grid(row=0, column=1, padx=(0, 6))
        ttk.Button(buttons, text="Cancel Scheduled", command=self.cancel_shutdown).grid(row=0, column=2)

        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(frame, textvariable=self.status_var).grid(row=4, column=0, columnspan=2, sticky="w")

        frame.columnconfigure(1, weight=1)

    @staticmethod
    def _format_duration(total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def _parse_delay_seconds(self):
        try:
            hours = int(self.hour_var.get().strip() or "0")
            minutes = int(self.minute_var.get().strip() or "0")
            seconds = int(self.second_var.get().strip() or "0")
        except ValueError:
            raise ValueError("Please enter valid numbers for hours, minutes, and seconds.")

        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Time values cannot be negative.")
        if minutes > 59 or seconds > 59:
            raise ValueError("Minutes and seconds must be between 0 and 59.")

        return (hours * 3600) + (minutes * 60) + seconds

    def schedule_shutdown(self):
        try:
            delay_seconds = self._parse_delay_seconds()
        except ValueError as error:
            messagebox.showerror("Invalid time", str(error))
            return

        if delay_seconds == 0:
            self.shutdown_now()
            return

        if not messagebox.askyesno("Confirm", f"Shutdown in {self._format_duration(delay_seconds)}?"):
            return

        self.cancel_shutdown(update_status=False)
        self.remaining_seconds = delay_seconds
        self.status_var.set(f"Shutdown scheduled in {self._format_duration(self.remaining_seconds)}")
        self.timer_id = self.root.after(1000, self._countdown)

    def _countdown(self):
        self.remaining_seconds -= 1
        if self.remaining_seconds <= 0:
            self.status_var.set("Shutting down now...")
            self._execute_shutdown()
            return

        self.status_var.set(f"Shutdown scheduled in {self._format_duration(self.remaining_seconds)}")
        self.timer_id = self.root.after(1000, self._countdown)

    def shutdown_now(self):
        if messagebox.askyesno("Confirm", "Shut down immediately?"):
            self.cancel_shutdown(update_status=False)
            self.status_var.set("Shutting down now...")
            self._execute_shutdown()

    def cancel_shutdown(self, update_status=True):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
            self.remaining_seconds = 0

        if update_status:
            self.status_var.set("Scheduled shutdown cancelled")

    def _execute_shutdown(self):
        try:
            shutdown_pc()
        except Exception as error:
            self.status_var.set("Error while shutting down")
            messagebox.showerror("Shutdown Error", str(error))


def main():
    root = tk.Tk()
    ShutdownGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()