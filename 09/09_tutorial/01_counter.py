# Počítadlo s tlačítkem pro reset.
# Přímá změna stavu okna.

from fmw import *

def reset_button(value):
    widget = button("Reset", 0)
    # print("Stav:", value)
    # print("Obsah okna:", widget)
    return widget

"""
display_window(reset_button, 4)
"""

def counter(value):
    label_value = label(str(value))
    inc_button = moved(button("+", value + 1), 0, 20)
    reset_button1 = moved(reset_button(value), 0, 50)
    
    buttons = group(inc_button, reset_button1)
    widget = group(label_value, buttons)
                   
    print("Stav:", value)
    print("Obsah okna:", widget)
    return widget

"""
display_window(counter, 0)
"""

