# Počítadla
from fmw import *
from lst import *

test_values = cons(0, cons(1, cons(5, empty)))

def counter(value):
    return group(label(str(value)),
                 moved(button("+", 1), 0, 20))

def counter_update(value, increment):
    return value + increment

# Změna akcí ovládacího prvku:
"""
>>> action_changed(button("+", 1), 0)
button('+', [0, 1], 0, 0)
"""

def counters(values, i=0):
    if is_empty(values):
        return empty_widget
    else:
        return group(action_changed(counter(first(values)), i),
                     moved(counters(rest(values), i + 1), 100, 0))
"""
>>> counters(test_values)
group(group(label('0', 0, 0),
            button('+', [0, 1], 0, 20)),
      group(group(label('1', 100, 0),
                  button('+', [1, 1], 100, 20)),
            group(group(label('5', 200, 0),
                        button('+', [2, 1], 200, 20)),
                  empty_widget)))
"""

# Změna prvku seznamu na indexu:
"""
>>> test_values
cons(0, cons(1, cons(5, empty)))
>>> list_change(test_values, 1, lambda x: x + 1)
cons(0, cons(2, cons(5, empty)))
"""

def counters_update_index(values, counter_index, increment):
    return list_change(values,
                       counter_index,
                       lambda value: counter_update(value, increment)) 

def update(values, action):
    print("Starý stav:", values)
    print("Akce:", action)
    return counters_update_index(values, action[0], action[1])

def content(values):
    widget = counters(values)
    print("Stav:", values)
    print("Obsah okna:", widget)
    return widget

# Počet počítadel:
counters_count = 3
display_window(content, list_constant(counters_count, 0), update)


