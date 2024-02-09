# Functional Micro Widget

# Jednoduchá knihovna na funkcionální uživatelské rozhraní.

import micro_widget as mw

class Label:
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text
    
    def __repr__(self):
        return f"label({repr(self.get_text())})"

    def create_mw(self, mw_window, origin):
        mw_widget = mw.make_label(mw_window)
        mw.set_label_text(mw_widget, self.get_text())
        mw.set_widget_x(mw_widget, origin[0])
        mw.set_widget_y(mw_widget, origin[1])
        return self

label = Label

def label_text(label):
    return label.get_text()

def is_label(value):
    return isinstance(value, Label) 

class Entry:
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text
    
    def __repr__(self):
        return f"entry({repr(self.get_text())})"

    def create_mw(self, mw_window, origin):
        mw_widget = mw.make_entry(mw_window)
        mw.set_entry_text(mw_widget, self.get_text())
        mw.set_widget_x(mw_widget, origin[0])
        mw.set_widget_y(mw_widget, origin[1])
        return self

entry = Entry

def entry_text(entry):
    return entry.get_text()

def is_entry(value):
    return isinstance(value, Entry)

class Button:
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text
    
    def __repr__(self):
        return f"button({repr(self.get_text())})"

    def create_mw(self, mw_window, origin):
        mw_widget = mw.make_button(mw_window)
        mw.set_button_text(mw_widget, self.get_text())
        mw.set_widget_x(mw_widget, origin[0])
        mw.set_widget_y(mw_widget, origin[1])
        return self

button = Button

def button_text(button):
    return button.get_text()

def is_button(value):
    return isinstance(value, Button)

class Checkbox:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value
    
    def __repr__(self):
        return f"checkbox({repr(self.get_value())})"

    def create_mw(self, mw_window, origin):
        mw_widget = mw.make_checkbox(mw_window)
        mw.set_checkbox_value(mw_widget, self.get_value())
        mw.set_widget_x(mw_widget, origin[0])
        mw.set_widget_y(mw_widget, origin[1])
        return self

checkbox = Checkbox

def checkbox_value(checkbox):
    return checkbox.get_value()

def is_checkbox(value):
    return isinstance(value, Checkbox)

class Radiobutton:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value
    
    def __repr__(self):
        return f"radiobutton({repr(self.get_value())})"

    def create_mw(self, mw_window, origin):
        mw_widget = mw.make_radiobutton(mw_window)
        mw.set_checkbox_value(mw_widget, self.get_value())
        mw.set_widget_x(mw_widget, origin[0])
        mw.set_widget_y(mw_widget, origin[1])
        return self

radiobutton = Radiobutton

checkbox = Checkbox

def radiobutton_value(radiobutton):
    return radiobutton.get_value()

def is_radiobutton(value):
    return isinstance(value, Radiobutton)



class Moved:
    def __init__(self, widget, dx, dy):
        self.widget = widget
        self.dx = dx
        self.dy = dy

    def get_widget(self):
        return self.widget
    
    def get_dx(self):
        return self.dx

    def get_dy(self):
        return self.dy

    def __repr__(self):
        widget = self.get_widget()
        dx = self.get_dx()
        dy = self.get_dy()
        return f"moved({widget}, {dx}, {dy})"

    def create_mw(self, mw_window, origin):
        widget = self.get_widget()
        dx = self.get_dx()
        dy = self.get_dy()
        new_origin = [origin[0] + dx, origin[1] + dy]
        widget.create_mw(mw_window, new_origin)
        return self

moved = Moved

def moved_widget(moved):
    return moved.get_widget()

def moved_dx(moved):
    return moved.get_dx()

def moved_dy(moved):
    return moved.get_dy()

def is_moved(value):
    return isinstance(value, Moved)

class Group:
    def __init__(self, widget1, widget2):
        self.item1 = widget1
        self.item2 = widget2

    def get_item1(self):
        return self.item1

    def get_item2(self):
        return self.item2

    def __repr__(self):
        item1 = self.get_item1()
        item2 = self.get_item2()
        return f"group({item1}, {item2})"

    def create_mw(self, mw_window, origin):
        item1 = self.get_item1()
        item2 = self.get_item2()
        item1.create_mw(mw_window, origin)
        item2.create_mw(mw_window, origin)
        return self

group = Group

def group_item1(group):
    return group.get_item1()

def group_item2(group):
    return group.get_item2()

def is_group(value):
    return isinstance(value, Group)

class EmptyWidget:
    def __repr__(self):
        return "empty_widget"

    def create_mw(self, mw_window, origin):
        return self

empty_widget = EmptyWidget()

def is_empty_widget(value):
    return value is empty_widget

def display_window(widget):
    mw_window = mw.display_window()
    widget.create_mw(mw_window, [0, 0])

def display_window_and_loop(widget):
    mw_window = mw.display_window()
    widget.create_mw(mw_window, [0, 0])
    mw.main_loop(mw_window)

"""
label1 = moved(label("světe!"), 100, 50)
button1 = moved(button("Ahoj"), 20, 10)
entry1 = moved(entry("Jméno"), 20, 100)
checkbox1 = moved(checkbox(True), 0, 0)
radiobutton1 = moved(radiobutton(False), 20, 0)
group1 = moved(group(checkbox1, radiobutton1), 10, 130)
widget1 = group(group(label1, button1),
                group(entry1, group1))
display_window_and_loop(widget1)
"""
