import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Define the path where the scripts are located (update if needed)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def run_script(script_name):
    """Helper function to run a script and handle errors."""
    script_path = os.path.join(SCRIPT_DIR, script_name)

    if not os.path.exists(script_path):
        messagebox.showerror("Error", f"File not found: {script_name}")
        return

    try:
        subprocess.Popen(["python", script_path])
        messagebox.showinfo("Success", f"{script_name} started successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run {script_name}: {e}")


# Initialize GUI
root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("400x300")

# Buttons to run different scripts
tk.Button(root, text="Train Model", command=lambda: run_script("train_model.py"), width=25).pack(pady=10)
tk.Button(root, text="Recognize Faces", command=lambda: run_script("face_recognition.py"), width=25).pack(pady=10)
tk.Button(root, text="Create Dataset", command=lambda: run_script("create_dataset.py"), width=25).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit, width=25).pack(pady=10)

root.mainloop()
