import pynput.keyboard as kb
import time

#  making keyboard controller to input keyboard commands
keyboard = kb.Controller()


def record():

    #  windows + g key to open game bar. this is more consistent than just using windows + alt + r
    keyboard.press(kb.Key.cmd)
    keyboard.press('g')
    time.sleep(0.5)
    keyboard.release(kb.Key.cmd)
    keyboard.release('g')

    #  windows + alt + R starts the game recorder in windows
    keyboard.press(kb.Key.cmd)
    keyboard.press(kb.Key.alt)
    keyboard.press('r')
    time.sleep(0.5)
    keyboard.release(kb.Key.cmd)
    keyboard.release(kb.Key.alt)
    keyboard.release('r')
