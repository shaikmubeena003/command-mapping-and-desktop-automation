# automation/mouse.py

import pyautogui

MOVE_DISTANCE = 100


def execute_mouse_command(command):
    """
    Execute mouse and scroll commands.
    """

    command = command.upper()

    try:

        if command == "LEFT":
            pyautogui.moveRel(-MOVE_DISTANCE, 0)

        elif command == "RIGHT":
            pyautogui.moveRel(MOVE_DISTANCE, 0)

        elif command == "UP":
            pyautogui.moveRel(0, -MOVE_DISTANCE)

        elif command == "DOWN":
            pyautogui.moveRel(0, MOVE_DISTANCE)

        elif command == "CLICK":
            pyautogui.click()

        elif command == "DOUBLE_CLICK":
            pyautogui.doubleClick()

        elif command == "SCROLL_UP":
            pyautogui.scroll(500)

        elif command == "SCROLL_DOWN":
            pyautogui.scroll(-500)

        else:
            return False, f"Unsupported mouse command: {command}"

        return True, f"{command} executed successfully"

    except Exception as e:
        return False, str(e)