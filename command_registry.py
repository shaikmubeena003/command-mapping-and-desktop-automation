COMMAND_REGISTRY = {
    #MEDIA AUTOMATION
    "PLAY":"MEDIA",
    "PAUSE":"MEDIA",
    "NEXT":"MEDIA",
    "PREVIOUS":"MEDIA",
    "VOLUME_UP":"MEDIA",
    "VOLUME_DOWN":"MEDIA",
    "MUTE":"MEDIA",

    #BROWSER AUTOMATION
    "OPEN_TAB":"BROWSER",
    "CLOSE_TAB":"BROWSER",  
    "NEXT_TAB":"BROWSER",
    "PREVIOUS_TAB":"BROWSER",
    "REFRESH":"BROWSER",

    #MOUSE AUTOMATION
    "LEFT":"MOUSE",
    "RIGHT":"MOUSE",
    "UP":"MOUSE",
    "DOWN":"MOUSE",
    "CLICK":"MOUSE",
    "DOUBLE_CLICK":"MOUSE",
    "SCROLL_UP":"MOUSE",
    "SCROLL_DOWN":"MOUSE",

    #APPLICATION AUTOMATION
    "OPEN_NOTEPAD":"APPLICATION",
    "CLOSE_NOTEPAD":"APPLICATION",
    "OPEN_CALCULATOR":"APPLICATION",
    "CLOSE_CALCULATOR":"APPLICATION",
    "SWITCH_WINDOW":"APPLICATION",
}
#helper functions

def get_command_category(command:str):
    return COMMAND_REGISTRY.get(command.upper())

def is_valid_command(command:str):
    return command.upper() in COMMAND_REGISTRY  