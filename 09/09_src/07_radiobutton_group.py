# Skupina přepínačů
from fmw import *
from lst import *

def radiobutton_group(count, selected, i=0):
    if count == i:
        return empty_widget
    else:
        return group(radiobutton(i == selected, i),
                     moved(radiobutton_group(count, selected, i + 1), 0, 20))

"""
>>> radiobutton_group(3, 2)
group(radiobutton(False, 0, 0, 0),
      group(radiobutton(False, 1, 0, 20),
            group(radiobutton(True, 2, 0, 40),
                  empty_widget)))
"""

def radiobutton_group_update(selected, index, is_selected):
    return index if is_selected else selected

# Počet přepínačů:
radiobuttons_count = 3

def content(selected):
    widget = radiobutton_group(radiobuttons_count, selected)
    print("Stav:", selected)
    print("Obsah okna:", widget)
    return widget
    
def update(selected, action):
    print("Starý stav:", selected)
    print("Akce:", action)
    return radiobutton_group_update(selected, action[0], action[1])

display_window(content, None, update)

