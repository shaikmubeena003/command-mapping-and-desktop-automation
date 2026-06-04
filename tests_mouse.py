# tests/test_mouse.py

import time
from automation.mouse import execute_mouse_command

print("=" * 50)
print("MOUSE & SCROLL AUTOMATION TEST")
print("=" * 50)

print("\nInstructions:")
print("1. Open any webpage or document")
print("2. Keep the mouse visible")
print("3. Testing will start in 10 seconds")

time.sleep(10)

commands = [
    "RIGHT",
    "LEFT",
    "DOWN",
    "UP",
    "CLICK",
    "DOUBLE_CLICK",
    "SCROLL_DOWN",
    "SCROLL_UP"
]

for command in commands:

    print(f"\nExecuting: {command}")

    success, message = execute_mouse_command(command)

    print(message)

    time.sleep(3)

print("\nMouse Automation Test Completed")