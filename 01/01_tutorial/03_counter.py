# Zobrazení hodnoty počítadla
import micro_widget as mw

# counter = ["counter", value, label]

def make_counter(window):
    label = mw.make_label(window)
    mw.set_label_text(label, "0")
    return ["counter", 0, label]

def get_counter_value(counter):
    return counter[1]

def set_counter_value(counter, value):
    label = counter[2]
    mw.set_label_text(label, str(value))
    counter[1] = value

# Používají abstraktní datovou strukturu counter:

def inc_counter(counter):
    set_counter_value(counter,
                      get_counter_value(counter) + 1)


def dec_counter(counter):
    set_counter_value(counter,
                      get_counter_value(counter) - 1)

"""
w = mw.display_window()
c = make_counter(w)
set_counter_value(c, 5)
"""

w = mw.display_window()
c = make_counter(w)
set_counter_value(c, 5)
inc_counter(c)

mw.main_loop(w)
