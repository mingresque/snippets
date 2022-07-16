# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 09:40:07 2022

@source: https://pynput.readthedocs.io/en/latest/keyboard.html

"""

from pynput import keyboard
import sys
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        #keyboard.
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_release=on_release)
listener.start()
listener.stop()

sys.exit(-1)
