import board
import usb_hid
from time import sleep

import adafruit_dotstar as dotstar
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse


# Objects for the mouse & keyboard emulation
mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Object for the RGB "Dotstar" LED on the Trinket
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)


# Countdown to start - give time for the OS to see the device
dot[0] = (15, 0, 0)
sleep(2)
dot[0] = (0, 0, 127)
sleep(2)
dot[0] = (0, 15, 0)
sleep(2)


# The main loop - hold the right mouse button for 2 minutes, then scan left and right
while True:

    dot[0] = (15, 0, 0)

    mouse.press(Mouse.RIGHT_BUTTON)
    sleep(120)
    mouse.release(Mouse.RIGHT_BUTTON)

    sleep(1)
    dot[0] = (0, 15, 0)

    key = Keycode.A
    keyboard.press(key)
    sleep(0.1)
    keyboard.release(key)

    sleep(0.3)
    dot[0] = (0, 0, 127)

    key = Keycode.D
    keyboard.press(key)
    sleep(0.1)
    keyboard.release(key)

    sleep(1)
