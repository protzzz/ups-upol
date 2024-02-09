# Počítadlo s tlačítkem pro reset.
# Akce tlačítka jsou pole,
# kde první prvek udává typ akce.

from fmw import *

buttons = group(button("+", ["inc", 1]),
                moved(button("Reset", ["reset"]), 0, 30))

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
    action_type = action[0]
    if action_type == "reset":
        return 0
    elif action_type == "inc":
        return update_counter_value(value, action[1])

# display_window_and_loop(buttons, 0, update)

display_window_and_loop(counter, 0, update)

