# Text a jeho převrácení
from fmw import *

def reverse_string(string):
    return string[::-1]

"""
>>> reverse_string("abc")
'cba'
"""

def entries(string):
    widget = group(entry(string, False),
                   moved(entry(reverse_string(string), True), 0, 40))
    print("Stav:", repr(string))
    print("Obsah okna:", widget)
    return widget

"""
>>> entries("abc")
group(entry('abc', False, 0, 0), entry('cba', True, 0, 40))
"""

def update_string(is_reversed, new_string):
    if is_reversed:
        return reverse_string(new_string)
    else:
        return new_string

"""
>>> update_string(True, "cba")
'abc'
>>> update_string(False, "abc")
'abc'
"""
    
def update_entries(string, action):
    print("Starý stav:", repr(string))
    print("Akce:", action)
    return update_string(action[0], action[1]) 

display_window_and_loop(entries, "", update_entries)

