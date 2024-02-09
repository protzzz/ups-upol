# Text a jeho délka
from fmw import *

def content(string):
    len_label = label(str(len(string)))
    widget = group(entry(string, True),
                   moved(len_label, 0, 30))
    print("Stav:", repr(string))
    print("Obsah okna:", widget)
    return widget

    
def update(string, action):
    print("Starý stav:", repr(string))
    print("Akce:", action)
    return action[1]

display_window_and_loop(content, "", update)

