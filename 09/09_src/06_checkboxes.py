# Zaškrtávací pole
from fmw import *
from lst import *

test_values = cons(True, cons(False, cons(True, empty)))

def checkboxes(values, i=0):
    if is_empty(values):
        return empty_widget
    else:
        return group(checkbox(first(values), i),
                     moved(checkboxes(rest(values), i + 1), 0, 20))

"""
>>> checkboxes(test_values)
group(checkbox(True, 0, 0, 0),
      group(checkbox(False, 1, 0, 20),
            group(checkbox(True, 2, 0, 40),
                  empty_widget)))
"""


# Změní prvek seznamu na indexu na zadanou hodnotu:
"""
>>> list_change_el(test_values, 1, True)
cons(True, cons(True, cons(True, empty)))
"""

def checkboxes_update(values, index, value):
    return list_change_el(values, index, value)

# int převede True na 1 a False na 0.
"""
>>> int(True)
1
>>> int(False)
0
"""

# Počet hodnot True v seznamu:
def list_count_trues(lst):
    return list_reduce(lambda v, s: int(v) + s, 0, lst)

"""
>>> list_count_trues(test_values)
2
"""

def content(values):
    count = list_count_trues(values)
    widget = group(moved(label(str(count)), 30, 0),
                   checkboxes(values))
    print("Stav:", values)
    print("Obsah okna:", widget)
    return widget

"""
>>> content(test_values)
group(label('2', 30, 0),
      group(checkbox(True, 0, 0, 0),
            group(checkbox(False, 1, 0, 20),
                  group(checkbox(True, 2, 0, 40),
                        empty_widget))))
"""

def update(values, action):
    print("Starý stav:", values)
    print("Akce:", action)
    return checkboxes_update(values, action[0], action[1])

# Počet zaškrtávacích polí:
checkbox_count = 3

# Vytvoří seznam o zadané délce:
"""
>>> list_constant(3, False)
cons(False, cons(False, cons(False, empty)))
"""
display_window(content, list_constant(checkbox_count, False), update)

