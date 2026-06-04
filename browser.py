# automation/browser.py

import pyautogui


def execute_browser_command(command):

    command = command.upper()

    try:

        if command == "OPEN_TAB":
            pyautogui.hotkey("ctrl", "t")

        elif command == "CLOSE_TAB":
            pyautogui.hotkey("ctrl", "w")

        elif command == "NEXT_TAB":
            pyautogui.hotkey("ctrl", "tab")

        elif command == "PREVIOUS_TAB":
            pyautogui.hotkey("ctrl", "shift", "tab")

        elif command == "REFRESH":
            pyautogui.press("f5")

        else:
            return False, f"Unsupported browser command: {command}"

        return True, f"{command} executed successfully"

    except Exception as e:
        return False, str(e)