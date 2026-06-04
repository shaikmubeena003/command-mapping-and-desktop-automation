# gui.py

import tkinter as tk
from tkinter import messagebox

from core.validator import validate_request
from core.dispatcher import dispatch_command


def execute_command():
    command = command_entry.get().strip().upper()

    if not command:
        messagebox.showwarning(
            "Warning",
            "Please enter a command."
        )
        return

    try:
        confidence = float(confidence_entry.get())
    except ValueError:
        messagebox.showerror(
            "Error",
            "Confidence must be a valid number."
        )
        return

    # Validate request
    is_valid, validation_message = validate_request(
        command,
        confidence
    )

    if not is_valid:
        result_label.config(
            text=f"❌ {validation_message}",
            fg="red"
        )
        return

    # Dispatch command
    success, execution_message = dispatch_command(command)

    if success:
        result_label.config(
            text=f"✅ {execution_message}",
            fg="green"
        )
    else:
        result_label.config(
            text=f"❌ {execution_message}",
            fg="red"
        )


def clear_fields():
    command_entry.delete(0, tk.END)
    confidence_entry.delete(0, tk.END)
    confidence_entry.insert(0, "0.95")

    result_label.config(
        text="Waiting for command...",
        fg="blue"
    )


# -----------------------------
# GUI WINDOW
# -----------------------------

root = tk.Tk()
root.title("Synapti Mesh - Command Console")
root.geometry("600x400")
root.resizable(False, False)

# Header
title_label = tk.Label(
    root,
    text="Synapti Mesh Command Console",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

subtitle_label = tk.Label(
    root,
    text="Day 2 - Command Mapping & Desktop Automation",
    font=("Arial", 10)
)
subtitle_label.pack()

# Command Section
command_frame = tk.Frame(root)
command_frame.pack(pady=20)

tk.Label(
    command_frame,
    text="Command:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10)

command_entry = tk.Entry(
    command_frame,
    width=30,
    font=("Arial", 12)
)
command_entry.grid(row=0, column=1)

# Confidence Section
confidence_frame = tk.Frame(root)
confidence_frame.pack(pady=10)

tk.Label(
    confidence_frame,
    text="Confidence:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10)

confidence_entry = tk.Entry(
    confidence_frame,
    width=30,
    font=("Arial", 12)
)
confidence_entry.insert(0, "0.95")
confidence_entry.grid(row=0, column=1)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

execute_button = tk.Button(
    button_frame,
    text="Execute Command",
    width=20,
    height=2,
    command=execute_command
)
execute_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=15,
    height=2,
    command=clear_fields
)
clear_button.grid(row=0, column=1, padx=10)

# Result Section
result_label = tk.Label(
    root,
    text="Waiting for command...",
    fg="blue",
    font=("Arial", 12, "bold")
)
result_label.pack(pady=20)

# Supported Commands
commands_text = """
Supported Commands

MEDIA:
PLAY, PAUSE, NEXT, PREVIOUS,
VOLUME_UP, VOLUME_DOWN, MUTE

BROWSER:
OPEN_TAB, CLOSE_TAB,
NEXT_TAB, PREVIOUS_TAB, REFRESH

MOUSE:
LEFT, RIGHT, UP, DOWN,
CLICK, DOUBLE_CLICK,
SCROLL_UP, SCROLL_DOWN

APPLICATION:
OPEN_NOTEPAD,
OPEN_CALCULATOR,
SWITCH_WINDOW
"""

commands_label = tk.Label(
    root,
    text=commands_text,
    justify="left",
    font=("Consolas", 9)
)
commands_label.pack(pady=10)

root.mainloop()