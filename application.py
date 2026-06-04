# automation/application.py

import subprocess
import pyautogui


def execute_application_command(command):
    """
    Execute application automation commands.
    """

    command = command.upper()

    try:

        if command == "OPEN_NOTEPAD":
            subprocess.Popen("notepad.exe")

        elif command == "OPEN_CALCULATOR":
            subprocess.Popen("calc.exe")

        elif command == "SWITCH_WINDOW":
            pyautogui.hotkey("alt", "tab")

        else:
            return False, f"Unsupported application command: {command}"

        return True, f"{command} executed successfully"

    except Exception as e:
        return False, str(e)