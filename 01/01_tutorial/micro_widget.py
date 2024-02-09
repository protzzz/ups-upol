# Knihovna Micro Widget

import tkinter as tk
from tkinter import ttk

# Micro widget value
MW_VALUE_TYPE_INDEX = 0
MW_VALUE_TK_OBJECT_INDEX = 1

def make_mw_value(widget_type, tk_object, *args):
    return [widget_type, tk_object, *args]

def get_value_tk_object(value):
    return value[MW_VALUE_TK_OBJECT_INDEX]

def get_mw_value_type(widget):
    return widget[MW_VALUE_TYPE_INDEX]

def is_mw_value(v):
    return type(v) == list and len(v) >= 2

def destroy_mw_value(value):
    tk_object = get_value_tk_object(value)
    tk_object.destroy()

    
# Window
_tk = None
TYPE_WINDOW = "window"
        
def display_window():
    global _tk
    if _tk:
        top = tk.Toplevel()
        def destroy_callback(*args):
            global _tk
            _tk = None
        top.bind("<Destroy>", destroy_callback)
    else:
        _tk = tk.Tk()
        top = _tk
    top.title("micro_widget window")
    top.geometry("297x210")
    return make_mw_value(TYPE_WINDOW, top)

def destroy_window(window):
    destroy_mw_value(window)
    
def is_window(value):
    return is_mw_value(value) and get_mw_value_type(value) == TYPE_WINDOW
    
def main_loop(window):
    get_value_tk_object(window).mainloop()


def call_after(delay, command):
    if not _tk:
        raise RuntimeError("No window displayed")
    _tk.after(delay, command)
    
# Widget
WIDGET_WINDOW_INDEX = 2
WIDGET_X_INDEX = 3
WIDGET_Y_INDEX = 4

def make_widget(widget_type, tk_object, window, *args):
    widget = make_mw_value(widget_type, tk_object, window, 0, 0, *args)
    tk_update_position(widget)
    return widget

def destroy_widget(widget):
    destroy_mw_value(widget)

def get_widget_window(widget):
    return widget[WIDGET_WINDOW_INDEX]

def get_widget_x(widget):
    return widget[WIDGET_X_INDEX]

def get_widget_y(widget):
    return widget[WIDGET_Y_INDEX]

def set_widget_x(widget, x):
    widget[WIDGET_X_INDEX] = x
    tk_update_position(widget)

def set_widget_y(widget, y):
    widget[WIDGET_Y_INDEX] = y
    tk_update_position(widget)

def tk_update_position(widget):
    x = get_widget_x(widget)
    y = get_widget_y(widget)
    get_value_tk_object(widget).place(x=x, y=y)
    
# Label
TYPE_LABEL = "label"
LABEL_TEXT_INDEX = 5
def make_label(window):
    tk_obj = ttk.Label(get_value_tk_object(window))
    return make_widget(TYPE_LABEL, tk_obj, window, "")

def is_label(value):
    return is_mw_value(value) and get_mw_value_type(value) == TYPE_LABEL

def set_label_text(label, text):
    label[LABEL_TEXT_INDEX] = text
    get_value_tk_object(label)["text"] = text

def get_label_text(label):
    return label[LABEL_TEXT_INDEX]

# Button
TYPE_BUTTON = "button"
BUTTON_TEXT_INDEX = 5
BUTTON_COMMAND_INDEX = 6

def make_button(window):
    tk_obj = ttk.Button(get_value_tk_object(window))
    button = make_widget(TYPE_BUTTON, tk_obj, window, "", empty_command)
    return button

def is_button(value):
    return is_mw_value(value) and get_mw_value_type(value) == TYPE_BUTTON

def set_button_text(button, text):
    button[BUTTON_TEXT_INDEX] = text
    get_value_tk_object(button)["text"] = text

def get_button_text(button):
    return button[BUTTON_TEXT_INDEX]

def set_button_command(button, command):
    tk_obj = get_value_tk_object(button)
    button[BUTTON_COMMAND_INDEX] = command
    tk_obj["command"] = command

def get_button_command(button):
    return button[BUTTON_COMMAND_INDEX]
    
# Entry
TYPE_ENTRY = "entry"
ENTRY_TEXT_INDEX = 5
ENTRY_VAR_INDEX = 6
ENTRY_COMMAND_INDEX = 7

def empty_command():
    pass

def make_entry(window):
    var = tk.StringVar()
    tk_obj = ttk.Entry(get_value_tk_object(window))
    entry = make_widget(TYPE_ENTRY, tk_obj, window, "", var, empty_command)
    tk_obj["textvariable"] = var
    def var_write_command(*args):
        entry[ENTRY_TEXT_INDEX] = var.get()
        entry[ENTRY_COMMAND_INDEX]()
    var.trace_add("write", var_write_command)
    return entry
    
def is_entry(value):
    return is_mw_value(value) and get_mw_value_type(value) == TYPE_ENTRY
    
def get_entry_text(entry):
    return entry[ENTRY_TEXT_INDEX]

def set_entry_text(entry, text):
    entry[ENTRY_TEXT_INDEX] = text 
    entry[ENTRY_VAR_INDEX].set(text)
    
def set_entry_command(entry, command):
    entry[ENTRY_COMMAND_INDEX] = command

def get_entry_command(entry):
    return entry[ENTRY_COMMAND_INDEX]

""" 
w = display_window()
l = make_label(w)
set_label_text(l, "Jméno:")
set_widget_x(l, 10)
set_widget_y(l, 10)
e = make_entry(w)
set_widget_x(e, 10)
set_widget_y(e, 30)
set_entry_text(e, "Josef")

def print_entry_text_command():
    print(get_entry_text(e))
    
set_entry_command(e, print_entry_text_command)
b = make_button(w)
set_button_text(b, "OK")

def button_command():
    print("Stisknuto")
    
set_button_command(b, button_command)
set_widget_x(b, 10)
set_widget_y(b, 60)
"""

