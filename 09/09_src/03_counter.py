# Počítadlo, kde se zpracovávají akce.
from fmw import *

def counter(value):
    widget = group(label(str(value)),
                   moved(button("+", 1), 0, 20))
    print("Stav:", value)
    print("Obsah okna:", widget)
    return widget
    
def update_counter_value(value, increment):
    print("Starý stav:", value)
    print("Akce:", increment)
    return value + increment 

display_window_and_loop(counter, 0, update_counter_value)

