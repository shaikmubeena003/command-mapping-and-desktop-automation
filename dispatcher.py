from core.command_registry import get_command_category

from automation.media import execute_media_command
from automation.browser import execute_browser_command
from automation.mouse import execute_mouse_command
from automation.application import execute_application_command


def dispatch_command(command):

    category = get_command_category(command)

    if category is None:
        return False, "Unknown Command"

    if category == "MEDIA":
        return execute_media_command(command)

    elif category == "BROWSER":
        return execute_browser_command(command)

    elif category == "MOUSE":
        return execute_mouse_command(command)

    elif category == "APPLICATION":
        return execute_application_command(command)

    return False, "Unsupported Category"