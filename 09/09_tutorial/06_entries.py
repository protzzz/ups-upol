# Dvě textová pole a délka obou řetězců.

from fmw import *

def len_label(strings):
    return label(str(len(strings[0]) + len(strings[1])))

"""
display_window(len_label(["A", "BC"]))
"""

def entries(strings):
    return group(entry(strings[0], 0),
                 moved(entry(strings[1], 1), 0, 30))

"""
display_window(entries(["A", "BC"]))
"""

def content(strings):
    widget = group(entries(strings),
                   moved(len_label(strings), 0, 60))
    print("Stav:", strings)
    print("Obsah okna:", widget)
    return widget

    
def update(strings, action):
    print("Starý stav:", strings)
    print("Akce:", action)
    if action[0] == 0:
        return [action[1], strings[1]]
    elif action[0] == 1:
        return [strings[0], action[1]]

display_window_and_loop(content, ["", ""], update)

