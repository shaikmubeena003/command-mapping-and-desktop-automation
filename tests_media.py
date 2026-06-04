# tests/test_media.py

import time
from automation.media import execute_media_command

print("=" * 50)
print("MEDIA AUTOMATION TEST")
print("=" * 50)

print("\nInstructions:")
print("1. Open YouTube / Spotify / VLC")
print("2. Start playing a song or video")
print("3. Switch to that window")
print("4. Testing will start in 10 seconds")

time.sleep(10)

commands = [
    "VOLUME_UP",
    "VOLUME_DOWN",
    "MUTE",
    "MUTE",
    "PLAY",
    "PLAY"
]

for command in commands:

    print(f"\nExecuting: {command}")

    success, message = execute_media_command(command)

    print(message)

    time.sleep(3)

print("\nMedia Automation Test Completed")