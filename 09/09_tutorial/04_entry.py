# Jedno textové pole.

from fmw import *

def content(string):
    widget = entry(string, True)
    print("Stav:", repr(string))
    print("Obsah okna:", widget)
    return widget

    
def update(string, action):
    print("Starý stav:", repr(string))
    print("Akce:", action)
    return action[1]

display_window_and_loop(content, "", update)

