import tkinter as tk
from tkinter import messagebox  # Import messagebox module explicitly
import threading
import os


class ShutdownApp:
    def __init__(self, master):
        self.master = master
        master.title("Shutdown Timer")

        self.label = tk.Label(master, text="Enter shutdown timer (in minutes):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.shutdown_btn = tk.Button(master, text="Shutdown", command=self.shutdown)
        self.shutdown_btn.pack()

        self.abort_btn = tk.Button(master, text="Abort", command=self.abort_shutdown)
        self.abort_btn.pack()

    def shutdown(self):
        try:
            timer_minutes = int(self.entry.get())
            timer_seconds = timer_minutes * 60
            threading.Timer(timer_seconds, self.execute_shutdown).start()
            messagebox.showinfo("Shutdown Timer", f"Shutdown in {timer_minutes} minutes.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def execute_shutdown(self):
        try:
            os.system(f"shutdown /s /t 1")  # Use f-string to include timer_seconds
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def abort_shutdown(self):
        try:
            os.system("shutdown /a")
            messagebox.showinfo("Shutdown Timer", "Shutdown aborted.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ShutdownApp(root)
    root.mainloop()
