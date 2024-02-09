import micro_widget as mw

w = mw.display_window()

l = mw.make_label(w)
mw.set_widget_x(l, 20)
mw.set_widget_y(l, 20)

b = mw.make_button(w)
mw.set_widget_x(b, 20)
mw.set_widget_y(b, 40)
mw.set_button_text(b, "+")

COUNTER_INDEX = 0
state = [None]

def set_counter(val):
    state[COUNTER_INDEX] = val
    mw.set_label_text(l, str(val))

def get_counter():
    return state[COUNTER_INDEX]

def inc_counter():
    set_counter(get_counter() + 1)
    
set_counter(0)
mw.set_button_command(b, inc_counter)

mw.main_loop(w)
