from pynput import keyboard
from pynput.keyboard import Listener, Controller, Key, KeyCode
import pyperclip

print("\nEnchanced Copy Paste")
print("To copy: command + c + [1,9]")
print("To paste: command + v + [1,9]")
print("To show current clipboard: a + s\n")

key_ctrl = Controller()

# The currently active keys
current = set()

# Stores our copy/pastes
strs = ["" for x in range(10)]

def copy(num):
    print("COPY" + str(num) + "!")
    strs[num] = pyperclip.paste()

def paste(num):
    print("PASTE" + str(num) + "!") 
    current.clear()
    for n in range(len(pyperclip.paste())):
        key_ctrl.press('\b')
        key_ctrl.release('\b')
    pyperclip.copy(strs[num])
    for char in pyperclip.paste():
        key_ctrl.press(char)
        key_ctrl.release(char)

def show():
     print (strs)

c1 = lambda : copy(1)
c2 = lambda : copy(2)
c3 = lambda : copy(3)
c4 = lambda : copy(4)
c5 = lambda : copy(5)
c6 = lambda : copy(6)
c7 = lambda : copy(7)
c8 = lambda : copy(8)
c9 = lambda : copy(9)

p1 = lambda : paste(1)
p2 = lambda : paste(2)
p3 = lambda : paste(3)
p4 = lambda : paste(4)
p5 = lambda : paste(5)
p6 = lambda : paste(6)
p7 = lambda : paste(7)
p8 = lambda : paste(8)
p9 = lambda : paste(9)

COMBINATIONS = {
    # command left
    frozenset([55, 8, 18]) : c1, # command + c + 1
    frozenset([55, 8, 19]) : c2, # command + c + 2
    frozenset([55, 8, 20]) : c3, # command + c + 3
    frozenset([55, 8, 21]) : c4, # command + c + 4
    frozenset([55, 8, 23]) : c5, # command + c + 5
    frozenset([55, 8, 22]) : c6, # command + c + 6
    frozenset([55, 8, 26]) : c7, # command + c + 7
    frozenset([55, 8, 28]) : c8, # command + c + 8
    frozenset([55, 8, 25]) : c9, # command + c + 9
    frozenset([55, 9, 18]) : p1, # command + v + 1
    frozenset([55, 9, 19]) : p2, # command + v + 2
    frozenset([55, 9, 20]) : p3, # command + v + 3
    frozenset([55, 9, 21]) : p4, # command + v + 4
    frozenset([55, 9, 23]) : p5, # command + v + 5
    frozenset([55, 9, 22]) : p6, # command + v + 6
    frozenset([55, 9, 26]) : p7, # command + v + 7
    frozenset([55, 9, 28]) : p8, # command + v + 8
    frozenset([55, 9, 25]) : p9, # command + v + 9
    frozenset([0, 1]): show, # show our current clipboard contents
    # command right
    frozenset([54, 8, 18]) : c1, # command + c + 1
    frozenset([54, 8, 19]) : c2, # command + c + 2
    frozenset([54, 8, 20]) : c3, # command + c + 3
    frozenset([54, 8, 21]) : c4, # command + c + 4
    frozenset([54, 8, 23]) : c5, # command + c + 5
    frozenset([54, 8, 22]) : c6, # command + c + 6
    frozenset([54, 8, 26]) : c7, # command + c + 7
    frozenset([54, 8, 28]) : c8, # command + c + 8
    frozenset([54, 8, 25]) : c9, # command + c + 9
    frozenset([54, 9, 18]) : p1, # command + v + 1
    frozenset([54, 9, 19]) : p2, # command + v + 2
    frozenset([54, 9, 20]) : p3, # command + v + 3
    frozenset([54, 9, 21]) : p4, # command + v + 4
    frozenset([54, 9, 23]) : p5, # command + v + 5
    frozenset([54, 9, 22]) : p6, # command + v + 6
    frozenset([54, 9, 26]) : p7, # command + v + 7
    frozenset([54, 9, 28]) : p8, # command + v + 8
    frozenset([54, 9, 25]) : p9, # command + v + 9
}

def get_vk(key):
    return key.vk if hasattr(key, 'vk') else key.value.vk

def on_press(key):
    print(key)
    vk = get_vk(key)
    current.add(vk)
    for combination in COMBINATIONS:
        if all(k in current for k in combination):
            print(current)
            COMBINATIONS[combination]()
            break

def on_release(key):
    try:
        vk = get_vk(key)
        current.remove(vk) # remove from current set
    except KeyError: 
        pass

# Listen for events
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()