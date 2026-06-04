from automation.browser import execute_browser_command
import time

print("Switch to browser in 5 seconds...")
time.sleep(5)

import webbrowser

def open_browser():
    webbrowser.open("https://google.com")

print(execute_browser_command("OPEN_TAB"))
print(execute_browser_command("REFRESH"))