# Počítadlo s tlačítky pro inkrementaci a dekrementaci.
from fmw import *

counter_buttons = group(button("+", 1),
                        moved(button("-", -1), 0, 30))

"""
display_window(counter_buttons)
"""

def counter(value):
    widget = group(label(str(value)),
                   moved(counter_buttons, 0, 20))
    print("Stav:", value)
    print("Obsah okna:", widget)
    return widget
    
def update_counter_value(value, increment):
    print("Starý stav:", value)
    print("Akce:", increment)
    return value + increment 

display_window(counter, 0, update_counter_value)

