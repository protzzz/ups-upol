# Prototyp Micro Widget

from proto import obj
import micro_widget as mw
import traceback


# prototyp pmw_object
pmw_object = obj.clone()
pmw_object.add_slot("delegate")

def pmw_object_send_event(call_super, self, event, *args):
    delegate = self
    while delegate:
        if delegate:
            if delegate.understand(event):
                delegate.send(event, self, *args)
        delegate = delegate.delegate()

pmw_object.set_slot("send_event", pmw_object_send_event)

# prototyp window
window = pmw_object.clone()
window.set_name("window")
window.add_slot("widget")
window.add_slot("mw_window")

def window_create_mw(call_super, self):
    widget = self.widget()
    if self.is_displayed() and widget != None:
        widget.create_mw(self.mw_window())
    return self

window.set_slot("create_mw", window_create_mw)

def window_display(call_super, self):
    mw_window = mw.display_window()
    self.set_mw_window(mw_window)
    self.create_mw()
    return self

window.set_slot("display", window_display)

def window_redisplay(call_super, self):
    self.destroy_mw()
    self.create_mw()
    return self

window.set_slot("redisplay", window_redisplay)

def window_is_displayed(call_super, self):
    return self.mw_window() != None

window.set_slot("is_displayed", window_is_displayed)

def window_clone(call_super, self):
    clone = call_super()
    clone.set_mw_window(None)
    widget = self.widget()
    if widget != None:
        clone.set_widget(widget.clone())
    return clone

window.set_slot("clone", window_clone)

def window_destroy_mw(call_super, self):
    if self.is_displayed() and self.widget():
        self.widget().destroy_mw()    
    return self

window.set_slot("destroy_mw", window_destroy_mw)


def window_set_widget(call_super, self, widget):
    self.destroy_mw()
    self.set_slot("widget", widget)
    if widget:
        widget.set_delegate(self)
    self.create_mw()
    return self

window.set_slot("set_widget", window_set_widget)

def window_main_loop(call_super, self):
    mw.main_loop(self.mw_window())
    return self

window.set_slot("main_loop", window_main_loop)

# prototyp widget
widget = pmw_object.clone()
widget.set_name("widget")

# prototyp atomic_widget
atomic_widget = widget.clone()
atomic_widget.set_name("atomic_widget")
atomic_widget.add_slot("x")
atomic_widget.add_slot("y")
atomic_widget.add_slot("mw_widget")
atomic_widget.set_x(0)
atomic_widget.set_y(0)

def atomic_widget_move(call_super, self, dx, dy):
    self.set_x(self.x() + dx)
    self.set_y(self.y() + dy)
    return self
    
atomic_widget.set_slot("move", atomic_widget_move)

def atomic_widget_destroy_mw(call_super, self):
    mw.destroy_widget(self.mw_widget())
    self.set_mw_widget(None)
    return self

atomic_widget.set_slot("destroy_mw", atomic_widget_destroy_mw)

def atomic_widget_update(call_super, self):
    mw_widget = self.mw_widget()
    if mw_widget:
        mw.set_widget_x(mw_widget, self.x())
        mw.set_widget_y(mw_widget, self.y())    
    return self

atomic_widget.set_slot("update", atomic_widget_update)

def atomic_widget_set_x(call_super, self, x):
    self.set_slot("x", x)
    self.update()
    return self

atomic_widget.set_slot("set_x", atomic_widget_set_x)

def atomic_widget_set_y(call_super, self, y):
    self.set_slot("y", y)
    self.update()
    return self

atomic_widget.set_slot("set_y", atomic_widget_set_y)

# prototyp texted_widget
texted_widget = atomic_widget.clone()
texted_widget.set_name("texted_widget")
texted_widget.add_slot("text")
texted_widget.set_text("")

def texted_widget_set_text(call_super, self, text):
    self.set_slot("text", text)
    self.update()
    return self

texted_widget.set_slot("set_text", texted_widget_set_text)
    

# prototyp label
label = texted_widget.clone()
label.set_name("label")

def label_create_mw(call_super, self, mw_window):
    mw_label = mw.make_label(mw_window)
    self.set_mw_widget(mw_label)
    self.update()
    return self

label.set_slot("create_mw", label_create_mw)

    
def label_update(call_super, self):
    call_super()
    mw_label = self.mw_widget()
    if mw_label:
        if mw.get_label_text(mw_label) != self.text():
            mw.set_label_text(mw_label, self.text())
    return self
    
label.set_slot("update", label_update)

# prototyp button
button = texted_widget.clone()
button.set_name("button")

def button_create_mw(call_super, self, mw_window):
    mw_button = mw.make_button(mw_window)
    self.set_mw_widget(mw_button)
    self.update()
    def command():
        self.send_event("ev_button_clicked")
    mw.set_button_command(mw_button, command)
    return self

button.set_slot("create_mw", button_create_mw)

    
def button_update(call_super, self):
    call_super()
    mw_label = self.mw_widget()
    if mw_label:
        mw.set_button_text(mw_label, self.text())
    return self
    
button.set_slot("update", button_update)

# prototyp entry
entry = texted_widget.clone()
entry.set_name("entry")

def entry_create_mw(call_super, self, mw_window):
    mw_entry = mw.make_entry(mw_window)
    def command():
        self.set_text(mw.get_entry_text(mw_entry))
        self.send_event("ev_entry_text_change")
    mw.set_entry_command(mw_entry, command)
    self.set_mw_widget(mw_entry)
    self.update()
    return self

entry.set_slot("create_mw", entry_create_mw)

    
def entry_update(call_super, self):
    call_super()
    mw_entry = self.mw_widget()
    if mw_entry:
        if mw.get_entry_text(mw_entry) != self.text():
            mw.set_entry_text(mw_entry, self.text())
    return self
    
entry.set_slot("update", entry_update)

# prototyp selectable_widget
selectable_widget = atomic_widget.clone()
selectable_widget.set_name("selectable_widget")
selectable_widget.add_slot("value")
selectable_widget.set_value(False)

def selectable_widget_set_value(call_super, self, value):
    self.set_slot("value", value)
    self.update()
    return self

selectable_widget.set_slot("set_value", selectable_widget_set_value)

# prototyp checkbox
checkbox = selectable_widget.clone()
checkbox.set_name("checkbox")

def checkbox_create_mw(call_super, self, mw_window):
    mw_checkbox = mw.make_checkbox(mw_window)
    def command():
        self.set_value(mw.get_checkbox_value(mw_checkbox))
        self.send_event("ev_checkbox_value_change")
    mw.set_checkbox_command(mw_checkbox, command)
    self.set_mw_widget(mw_checkbox)
    self.update()
    return self

checkbox.set_slot("create_mw", checkbox_create_mw)

    
def checkbox_update(call_super, self):
    call_super()
    mw_checkbox = self.mw_widget()
    if mw_checkbox:
        if mw.get_checkbox_value(mw_checkbox) != self.value():
            mw.set_checkbox_value(mw_checkbox, self.value())
    return self
    
checkbox.set_slot("update", checkbox_update)

# prototyp radiobutton
radiobutton = selectable_widget.clone()
radiobutton.set_name("radiobutton")

def radiobutton_create_mw(call_super, self, mw_window):
    mw_radiobutton = mw.make_radiobutton(mw_window)
    def command():
        self.set_value(mw.get_radiobutton_value(mw_radiobutton))
        self.send_event("ev_radiobutton_value_change")
    mw.set_radiobutton_command(mw_radiobutton, command)
    self.set_mw_widget(mw_radiobutton)
    self.update()
    return self

radiobutton.set_slot("create_mw", radiobutton_create_mw)

    
def radiobutton_update(call_super, self):
    call_super()
    mw_radiobutton = self.mw_widget()
    if mw_radiobutton:
        if mw.get_radiobutton_value(mw_radiobutton) != self.value():
            mw.set_radiobutton_value(mw_radiobutton, self.value())
    return self
    
radiobutton.set_slot("update", radiobutton_update)

# prototyp group
group = widget.clone()
group.set_name("group")
group.add_slot("items")
group.set_items([])


def group_clone(call_super, self):
    clone = call_super()
    # Klon skupiny není v okně:
    clone.set_delegate(None)
    clone.set_mw_window(None)
    cloned_items = []
    for item in self.items():
        cloned_items += [item.clone()]
    #clone.set_slot("items", []) # Zamezí odstranění původních prvků


    clone.set_items(cloned_items)
    return clone

group.set_slot("clone", group_clone)


def group_move(call_super, self, dx, dy):
    for item in self.items():
        item.move(dx, dy)
    return self

group.set_slot("move", group_move)

group.add_slot("mw_window")

def group_create_mw(call_super, self, mw_window):
    self.create_mw_items(mw_window)
    self.set_mw_window(mw_window)
    return self

group.set_slot("create_mw", group_create_mw)

def group_create_mw_items(call_super, self, mw_window):
    for item in self.items():
        item.create_mw(mw_window)
    return self

group.set_slot("create_mw_items", group_create_mw_items)

def group_destroy_mw(call_super, self):
    self.destroy_mw_items()
    self.set_mw_window(None)
    return self

group.set_slot("destroy_mw", group_destroy_mw)

def group_destroy_mw_items(call_super, self):
    for item in self.items():
        item.destroy_mw()
    return self

group.set_slot("destroy_mw_items", group_destroy_mw_items)

def group_set_items(call_super, self, items):
    if self.mw_window():
        self.destroy_mw_items()
    self.set_slot("items", items)
    for item in items:
        item.set_delegate(self)
    if self.mw_window():
        self.create_mw_items(self.mw_window())
    return self

group.set_slot("set_items", group_set_items)

def group_update(call_super, self):
    for item in self.items():
        item.update()
    return self

group.set_slot("update", group_update)

"""
w = window.clone()
b = button.clone()
w.set_widget(b)
w.display()
"""
