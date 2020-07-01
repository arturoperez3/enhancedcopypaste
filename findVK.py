from pynput import keyboard
from pynput.keyboard import Listener, Controller, Key, KeyCode

# Short script to find the virtual key numbers for your specific machine 

def on_press(key):
    vk = key.vk if hasattr(key, 'vk') else key.value.vk
    print("key: " + str(key) + " vk = " + str(vk))   

def on_release(key):
    print()

# Listen for events
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
