# enhancedcopypaste
Hold up to 12 items for copy/paste in your clipboard at once.

Using our favorite key bindings command+c and command+v to access the Copy/Paste clipboard, this scripts "extends" the clipboards capability to hold 12 items. 

In reality, when we copy, we fetch the OS clipboard contents and put it into a list. Then, when we paste, we retrieve the content from our list and load it back into the OS clipboard, which then gets pasted (you'll notice that the clipboard will paste what it originally held, only to be replaced by what was retrieved from the list). 

I originally used command + [0,9], but because these are typically their own hotkeys in all sorts of applications (I'm looking at you Chrome), they proved unreliable and led to all sorts of out of control behavior.

I have migrated to use function keys 1-12 instead to avoid undefined behavior. 

## Key Bindings: 

command + c + [f1, f12] (store into one of 12 cells)

command + v + [f1, f12] (retrieve from one of 12 cells)

a + s (show contents of our clipboard)

## Example Use: 
run: `python enhancedcopypaste.py`

### To copy:

Lorem (command + c + f1)

ipsum (command + c + f2)

dolor (command + c + f3)

sit amet, (command + c + f7)

agam noster id  (command + c + f11)

### To see contents:

['Lorem', 'ipsum', 'dolor', '', '', '', 'sit amet,', '', '', '', 'agam noster id', '']  (a + s)

### To paste:

agam noster id  (command + v + f11)

sit amet, (command + v + f7)

Lorem (command + v + f1)

ipsum (command + v + f2)

dolor   (command + v + f3) 


Inspired by my friend Austin.
