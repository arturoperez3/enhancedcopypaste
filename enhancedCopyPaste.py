from pynput import keyboard
from pynput.keyboard import Listener, Controller, Key, KeyCode
import pyperclip

print("\nEnhanced Copy Paste")
print("To copy: command + c + [F1,F12]")
print("To paste: command + v + [F1,F12]")
print("To show current clipboard: a + s\n")

# Access keyboard
key_ctrl = Controller()

# The currently active keys,
# allows us to build combinations
current = set()

# Stores our copy/pastes
strs = ["" for x in range(12)]

def copy(num):
    print("COPY" + str(num+1) + "!")
    strs[num] = pyperclip.paste() # fetch from OS clipboard

def paste(num):
    print("PASTE" + str(num+1) + "!")
    current.clear()
    
    # delete original paste
    for n in range(len(pyperclip.paste())):
        key_ctrl.press('\b')
        key_ctrl.release('\b')
        
    # fetch requested paste
    pyperclip.copy(strs[num])
    for char in pyperclip.paste():
        key_ctrl.press(char)
        key_ctrl.release(char)

def show():
     print (strs)

c0 = lambda : copy(0)
c1 = lambda : copy(1)
c2 = lambda : copy(2)
c3 = lambda : copy(3)
c4 = lambda : copy(4)
c5 = lambda : copy(5)
c6 = lambda : copy(6)
c7 = lambda : copy(7)
c8 = lambda : copy(8)
c9 = lambda : copy(9)
c10 = lambda : copy(10)
c11 = lambda : copy(11)

p0 = lambda : paste(0)
p1 = lambda : paste(1)
p2 = lambda : paste(2)
p3 = lambda : paste(3)
p4 = lambda : paste(4)
p5 = lambda : paste(5)
p6 = lambda : paste(6)
p7 = lambda : paste(7)
p8 = lambda : paste(8)
p9 = lambda : paste(9)
p10 = lambda : paste(10)
p11 = lambda : paste(11)

COMBINATIONS = {
    # command left
    frozenset([55, 8, 122]) : c0, # command + c + f1
    frozenset([55, 8, 120]) : c1, # command + c + f2
    frozenset([55, 8, 99]) : c2, # command + c + f3
    frozenset([55, 8, 118]) : c3, # command + c + f4
    frozenset([55, 8, 96]) : c4, # command + c + f5
    frozenset([55, 8, 97]) : c5, # command + c + f6
    frozenset([55, 8, 98]) : c6, # command + c + f7
    frozenset([55, 8, 100]) : c7, # command + c + f8
    frozenset([55, 8, 101]) : c8, # command + c + f9
    frozenset([55, 8, 109]) : c9, # command + c + f10
    frozenset([55, 8, 103]) : c10, # command + c + f11
    frozenset([55, 8, 111]) : c11, # command + c + f12
    frozenset([55, 9, 122]) : p0, # command + v + f1
    frozenset([55, 9, 120]) : p1, # command + v + f2
    frozenset([55, 9, 99]) : p2, # command + v + f3
    frozenset([55, 9, 118]) : p3, # command + v + f4
    frozenset([55, 9, 96]) : p4, # command + v + f5
    frozenset([55, 9, 97]) : p5, # command + v + f6
    frozenset([55, 9, 98]) : p6, # command + v + f7
    frozenset([55, 9, 100]) : p7, # command + v + f8
    frozenset([55, 9, 101]) : p8, # command + v + f9
    frozenset([55, 9, 109]) : p9, # command + v + f10
    frozenset([55, 9, 103]) : p10, # command + v + f11
    frozenset([55, 9, 111]) : p11, # command + v + f12
    frozenset([0, 1]): show, # show our current clipboard contents
    # command right
    frozenset([54, 8, 122]) : c0, # command + c + f1
    frozenset([54, 8, 120]) : c1, # command + c + f2
    frozenset([54, 8, 99]) : c2, # command + c + f3
    frozenset([54, 8, 118]) : c3, # command + c + f4
    frozenset([54, 8, 96]) : c4, # command + c + f5
    frozenset([54, 8, 97]) : c5, # command + c + f6
    frozenset([54, 8, 98]) : c6, # command + c + f7
    frozenset([54, 8, 100]) : c7, # command + c + f8
    frozenset([54, 8, 101]) : c8, # command + c + f9
    frozenset([54, 8, 109]) : c9, # command + c + f10
    frozenset([54, 8, 103]) : c10, # command + c + f11
    frozenset([54, 8, 111]) : c11, # command + c + f12
    frozenset([54, 9, 122]) : p0, # command + v + f1
    frozenset([54, 9, 120]) : p1, # command + v + f2
    frozenset([54, 9, 99]) : p2, # command + v + f3
    frozenset([54, 9, 118]) : p3, # command + v + f4
    frozenset([54, 9, 96]) : p4, # command + v + f5
    frozenset([54, 9, 97]) : p5, # command + v + f6
    frozenset([54, 9, 98]) : p6, # command + v + f7
    frozenset([54, 9, 100]) : p7, # command + v + f8
    frozenset([54, 9, 101]) : p8, # command + v + f9
    frozenset([54, 9, 109]) : p9, # command + v + f10
    frozenset([54, 9, 103]) : p10, # command + v + f11
    frozenset([54, 9, 111]) : p11, # command + v + f12
}

# get virtual key value of key press
def get_vk(key):
    return key.vk if hasattr(key, 'vk') else key.value.vk

# when a key is pressed
def on_press(key):
    print(key)
    vk = get_vk(key)
    current.add(vk) # so we can build combinations
    for combination in COMBINATIONS:
        if all(k in current for k in combination):
            print(current)
            COMBINATIONS[combination]()
            break

# when a key is released
def on_release(key):
    try:
        vk = get_vk(key)
        current.remove(vk) # remove key from current set
    except KeyError: 
        pass

# Listen for key presses
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
