# Počítadlo s tlačítkem pro reset.
# Akce tlačítka se rozlišují podle typu hodnoty.

from fmw import *

buttons = group(button("+", 1),
                moved(button("Reset", "reset"), 0, 30))

"""
display_window(buttons, 0, update)
"""

def counter(value):
    widget = group(label(str(value)),
                   moved(buttons, 0, 20))
    print("Stav:", value)
    print("Obsah okna:", widget)
    return widget
    
def update_counter_value(value, increment):
    return value + increment

def update(value, action):
    print("Starý stav:", value)
    print("Akce:", action)
    if action == "reset":
        return 0
    else:
        return update_counter_value(value, action)

display_window(counter, 0, update)

