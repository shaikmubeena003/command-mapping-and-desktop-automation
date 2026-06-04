# automation/media.py

import pyautogui


def execute_media_command(command):
    """
    Execute media control commands.

    Supported Commands:
    PLAY
    PAUSE
    NEXT
    PREVIOUS
    VOLUME_UP
    VOLUME_DOWN
    MUTE
    """

    command = command.upper()

    media_actions = {
        "PLAY": "playpause",
        "PAUSE": "playpause",
        "NEXT": "nexttrack",
        "PREVIOUS": "prevtrack",
        "VOLUME_UP": "volumeup",
        "VOLUME_DOWN": "volumedown",
        "MUTE": "volumemute"
    }

    if command not in media_actions:
        return False, f"Unsupported media command: {command}"

    try:
        pyautogui.press(media_actions[command])
        return True, f"{command} executed successfully"

    except Exception as e:
        return False, str(e)