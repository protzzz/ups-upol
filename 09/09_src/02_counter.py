# Počítadlo, které mění přímo stav okna.
from fmw import *

def counter(value):
    widget = group(label(str(value)),
                   moved(button("+", value + 1), 0, 20))
    print("Stav:", value)
    print("Obsah okna:", widget)
    return widget

"""
>>> counter(0)
group(label('0', 0, 0), button('+', 1, 0, 20))
>>> counter(1)
group(label('1', 0, 0), button('+', 2, 0, 20))
>>> display_window(counter(0))
>>> display_window(counter, 0)
"""

