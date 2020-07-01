from pynput import keyboard
from pynput.keyboard import Listener, Controller
import pyperclip

print("Enchanced Copy paste")
print("To copy: command + c + [0,9]")
print("To paste: command + [0,9] + v")
print("To show current clipboard: a + s")

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
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('c'), keyboard.KeyCode.from_char('1')]) : c1,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('c'), keyboard.KeyCode.from_char('2')]) : c2,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('c'), keyboard.KeyCode.from_char('3')]) : c3,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('c'), keyboard.KeyCode.from_char('4')]) : c4,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('c'), keyboard.KeyCode.from_char('5')]) : c5,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('c'), keyboard.KeyCode.from_char('6')]) : c6,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('c'), keyboard.KeyCode.from_char('7')]) : c7,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('c'), keyboard.KeyCode.from_char('8')]) : c8,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('c'), keyboard.KeyCode.from_char('9')]) : c9,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('v'), keyboard.KeyCode.from_char('1')]) : p1,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('v'), keyboard.KeyCode.from_char('2')]) : p2,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('v'), keyboard.KeyCode.from_char('3')]) : p3,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('v'), keyboard.KeyCode.from_char('4')]) : p4,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('v'), keyboard.KeyCode.from_char('5')]) : p5,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('v'), keyboard.KeyCode.from_char('6')]) : p6,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('v'), keyboard.KeyCode.from_char('7')]) : p7,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('v'), keyboard.KeyCode.from_char('8')]) : p8,
    frozenset([keyboard.Key.cmd, keyboard.KeyCode.from_char('v'), keyboard.KeyCode.from_char('9')]) : p9,
    frozenset([keyboard.KeyCode.from_char('a'), keyboard.KeyCode.from_char('s')]): show,
}

# On key press
def on_press(key):
    vk = key.vk if hasattr(key, 'vk') else key.value.vk
    print('vk =', vk)
    current.add(key)
    for combination in COMBINATIONS:
        print(key)
        if all(k in current for k in combination):
            print(current)
            print("THE INFINITE LOOP IS HERE")
            COMBINATIONS[combination]()
            break

# On key release
def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

# Listen for events
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()