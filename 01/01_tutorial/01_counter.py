# Počítadlo s tlačítkem minus
import micro_widget as mw

w = mw.display_window()

l = mw.make_label(w)
mw.set_widget_x(l, 20)
mw.set_widget_y(l, 20)

b1 = mw.make_button(w)
mw.set_widget_x(b1, 20)
mw.set_widget_y(b1, 40)
mw.set_button_text(b1, "+")

b2 = mw.make_button(w)
mw.set_widget_x(b2, 20)
mw.set_widget_y(b2, 70)
mw.set_button_text(b2, "-")

COUNTER_INDEX = 0
state = [None]

def set_counter(val):
    state[COUNTER_INDEX] = val
    mw.set_label_text(l, str(val))

def get_counter():
    return state[COUNTER_INDEX]

def inc_counter():
    set_counter(get_counter() + 1)

def dec_counter():
    set_counter(get_counter() - 1)
    
set_counter(0)
mw.set_button_command(b1, inc_counter)
mw.set_button_command(b2, dec_counter)

mw.main_loop(w)
