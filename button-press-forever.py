#!/usr/bin/python3

import asyncio
import evdev
from evdev.ecodes import EV_KEY
import sys
import os

async def run_command(device, command):
    """
    This function waits for button presses and
    executes a shell command when the button is pressed.
    """
    print("Waiting for button presses ...")
    async for event in device.async_read_loop():
        if EV_KEY == event.type:
            key_event = evdev.KeyEvent(event)
            if evdev.KeyEvent.key_down == key_event.keystate:
                os.system(command)

if __name__ == '__main__':

    if len(sys.argv) != 3:
        raise RuntimeError("Incorrect number of arguments")

    device_path = sys.argv[1]
    command = sys.argv[2]

    if not os.path.exists(device_path):
        raise RuntimeError(f"Device '{device}' does not exist")

    device = evdev.InputDevice(device_path)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_command(device, command))
    loop.close()

    device.close()