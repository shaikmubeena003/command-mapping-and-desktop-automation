# tests/test_application.py

import time
from automation.application import execute_application_command

print("=" * 50)
print("APPLICATION AUTOMATION TEST")
print("=" * 50)

print("\nInstructions:")
print("1. Minimize unnecessary windows")
print("2. Keep desktop visible")
print("3. Testing will start in 10 seconds")

time.sleep(10)

commands = [
    "OPEN_NOTEPAD",
    "OPEN_CALCULATOR",
    "SWITCH_WINDOW"
]

for command in commands:

    print(f"\nExecuting: {command}")

    success, message = execute_application_command(command)

    print(message)

    time.sleep(5)

print("\nApplication Automation Test Completed")