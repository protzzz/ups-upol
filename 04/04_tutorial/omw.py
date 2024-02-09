# Knihovna Object Micro Widget verze 2
import micro_widget as mw

class OMWObject:
    def __init__(self):
        self.delegate = None
        self.change_level = 0
    
    def get_delegate(self):
        return self.delegate

    def set_delegate(self, delegate):
        self.delegate = delegate
        return self

    def get_change_level(self):
        return self.change_level
    
    def inc_change_level(self):
        self.change_level += 1
        return self

    def dec_change_level(self):
        self.change_level -= 1
        return self

    def handle_event(self, event, args):
        if hasattr(self, event):
            handler = getattr(self, event)
            return handler(*args)

    def delegate_propagate_event(self, event, args):
        delegate = self.get_delegate()
        if delegate:
            delegate.propagate_event(event, args)

    def propagate_event(self, event, args):
        stop_propagation = self.handle_event(event, args)
        self.delegate_propagate_event(event, args)
            
    def send_event(self, event, *event_args):
        #args = [self] + list(event_args)
        delegate = self.get_delegate()
        if delegate:
            if hasattr(delegate, event):
                handler = getattr(delegate, event)
                return handler(self, *event_args)
        #self.propagate_event(event, args)
        return self

    def changing(self):
        if self.get_change_level() == 0:
            self.send_event("ev_changing")
        self.inc_change_level()
        
    def change(self):
        self.dec_change_level()
        if self.get_change_level() == 0:
            self.send_event("ev_change")
        return self

    def ev_changing(self, sender):
        return self.changing()

    def ev_change(self, sender):
        return self.change()

    def ev_button_clicked(self, sender, button):
        return self.send_event("ev_button_clicked", button)
        

        
class MWValue:
    def __init__(self):
        super().__init__()
        self.mw_value = None

    def get_mw_value(self):
        return self.mw_value

    def set_mw_value(self, mw_value):
        self.mw_value = mw_value
        return self

    def destroy_mw_value(self):
        raise NotImplementedError("Method has to be rewritten.")
        
    def delete_mw_value(self):
        self.destroy_mw_value()
        self.set_mw_value(None)
        return self

    def make_mw_value(self, root):
        raise NotImplementedError("Method has to be rewritten.")

    def create_mw_value(self):
        self.set_mw_value(self.make_mw_value(self.get_mw_window()))
        return self



class Widget(OMWObject):
    def __init__(self):
        super().__init__()
        self.mw_window = None

    def get_mw_window(self):
        return self.mw_window

    def set_mw_window(self, mw_window):
        self.mw_window = mw_window
        return self

    def create_mw_values(self, mw_window):
        self.set_mw_window(mw_window)
        self.create_mw_value()
        return self

    def destroy_mw_values(self):
        self.destroy_mw_value()
        self.set_mw_window(None)
        return self

    def is_mw_displayed(self):
        return self.get_mw_window() != None
        


class AtomicWidget(MWValue, Widget):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def get_x(self):
        return self.x

    def do_set_x(self, x):
        self.x = x
        if self.is_mw_displayed():
            self.mw_update_position()
        return self

    def set_x(self, x):
        try:
            self.changing()
            self.do_set_x(x)
        finally:
            self.change()
        return self

    def get_y(self):
        return self.y

    def do_set_y(self, y):
        self.y = y
        if self.is_mw_displayed():
            self.mw_update_position()
        return self

    def set_y(self, y):
        try:
            self.changing()
            self.do_set_y(y)
        finally:
            self.change()
        return self

    def mw_update_position(self):
        mw_widget = self.get_mw_value()
        mw.set_widget_x(mw_widget, self.get_x())
        mw.set_widget_y(mw_widget, self.get_y())
        return self
    
    def do_move(self, dx, dy):
        self.set_x(self.get_x() + dx)
        self.set_y(self.get_y() + dy)
        return self

    def move(self, dx, dy):
        try:
            self.changing()
            self.do_move(dx, dy)
        finally:
            self.change()
        return self

    def create_mw_value(self):
        super().create_mw_value()
        self.mw_update_position()
        return self
        
    
    
class Window(MWValue, OMWObject):
    def __init__(self):
        super().__init__()
        self.widget = None
        self.create_mw_value()

    # micro widget
    def get_mw_window(self):
        return self.get_mw_value()
    
    def make_mw_value(self, root):
        return mw.display_window()
    
    # vlastnost widget
    
    def get_widget(self):
        return self.widget

    def do_set_widget(self, widget):     
        old_widget = self.get_widget()
        if old_widget:
            old_widget.destroy_mw_values()
            old_widget.set_delegate(None)

        self.widget = widget
        
        if widget:
            widget.set_delegate(self)
            widget.create_mw_values(self.get_mw_value())
        return self
    
    def set_widget(self, widget):
        try:
            self.changing()
            self.do_set_widget(widget)
        finally:
            self.change()
        return self

    def main_loop(self):
        mw.main_loop(self.get_mw_value())
        return self

    def destroy(self):
        mw.destroy_window(self.get_mw_value())
        return self

class Texted:
    def __init__(self):
        super().__init__()
        self.text = ""

    # micro widget
    def mw_set_text(self, text):
        raise NotImplementedError("Method has to be rewritten.")
    
    def mw_update_text(self):
        self.mw_set_text(self.get_text())
        return self
        
    def create_mw_value(self):
        super().create_mw_value()
        self.mw_update_text()
        return self

    # vlastnosti
    def get_text(self):
        return self.text

    def do_set_text(self, text):
        self.text = text
        if self.is_mw_displayed():
            self.mw_update_text()
        return self

    def set_text(self, text):
        try:
            self.changing()
            self.do_set_text(text)
        finally:
            self.change()
        return self

class TextedWidget(Texted, AtomicWidget):
    pass

class Label(TextedWidget):
    # micro widget
    def make_mw_value(self, mw_window):
        return mw.make_label(mw_window)

    def mw_set_text(self, text):
        mw_label = self.get_mw_value()
        mw.set_label_text(mw_label, text)
        return self

class Button(TextedWidget):
    # micro widget
    def make_mw_value(self, window):
        return mw.make_button(window)

    def mw_set_text(self, text):
        mw_value = self.get_mw_value()
        mw.set_button_text(mw_value, text)
        
    def create_mw_value(self):
        super().create_mw_value()
        def click_command():
            self.button_clicked() 
        mw.set_button_command(self.get_mw_value(), click_command)
        return self

    # události
    def button_clicked(self):
        self.send_event("ev_button_clicked", self)
        return self




class Entry(TextedWidget):
    # micro widget
    def make_mw_value(self, mw_window):
        e = mw.make_entry(mw_window)
        return e
    
    def create_mw_value(self):
        super().create_mw_value()
        mw_entry = self.get_mw_value()
        def change_command():
            self.set_text(mw.get_entry_text(mw_entry))
        mw.set_entry_command(mw_entry, change_command)
        return self

    def mw_set_text(self, text):
        mw_entry = self.get_mw_value()
        mw.set_entry_text(mw_entry, text)
        return self


class BooleanValued:
    def __init__(self):
        super().__init__()
        self.value = False

    # micro widget
    def mw_set_value(self, value):
        raise NotImplementedError("Method has to be rewritten.")
    
    def mw_update_value(self):
        self.mw_set_value(self.get_value())
        return self
        
    def create_mw_value(self):
        super().create_mw_value()
        self.mw_update_value()
        return self

    # vlastnosti
    def get_value(self):
        return self.value

    def do_set_value(self, value):
        self.value = value
        if self.is_mw_displayed():
            self.mw_update_value()
        return self

    def set_value(self, value):
        try:
            self.changing()
            self.do_set_value(value)
        finally:
            self.change()
        return self

    def is_selected(self):
        return self.get_value()

    def toggle(self):
        self.set_value(not self.get_value())
        return self

class SelectableWidget(BooleanValued, AtomicWidget):
    pass

class Checkbox(SelectableWidget):
    # micro widget
    def make_mw_value(self, mw_window):
        e = mw.make_checkbox(mw_window)
        return e
    
    def create_mw_value(self):
        super().create_mw_value()
        mw_checkbox = self.get_mw_value()
        def change_command():
            self.set_value(mw.get_checkbox_value(mw_checkbox))
        mw.set_checkbox_command(mw_checkbox, change_command)
        return self

    def mw_set_value(self, value):
        mw_checkbox = self.get_mw_value()
        mw.set_checkbox_value(mw_checkbox, value)
        return self

class Radiobutton(SelectableWidget):
    # micro widget
    def make_mw_value(self, mw_window):
        e = mw.make_radiobutton(mw_window)
        return e
    
    def create_mw_value(self):
        super().create_mw_value()
        mw_radiobutton = self.get_mw_value()
        def change_command():
            self.set_value(mw.get_radiobutton_value(mw_radiobutton))
        mw.set_radiobutton_command(mw_radiobutton, change_command)
        return self

    def mw_set_value(self, value):
        mw_radiobutton = self.get_mw_value()
        mw.set_radiobutton_value(mw_radiobutton, value)
        return self 

class CompoundWidget(Widget):
    def __init__(self):
        super().__init__()
        self.items = []

    def get_items(self):
        return self.items[:]

    def check_item(self, item):
        if not isinstance(item, Widget):
            raise TypeError("Items have to be widgets.")
    
    def check_items(self, items):
        for item in items:
            self.check_item(item)
        return self

    def do_set_items(self, items):
        self.check_items(items)
        self.set_items_delegate(None)
        self.items = items[:]
        self.set_items_delegate(self)
        return self

    def set_items(self, items):
        try:
            self.changing()
            self.do_set_items(items)
        finally:
            self.change()
        return self

    def is_mw_displayed(self):
        return self.get_mw_window() != None
        
    def set_items_delegate(self, delegate):
        for item in self.get_items():
            item.set_delegate(delegate)
        return self

    def create_mw_value(self):
        return self

    def destroy_mw_value(self):
        return self
    
    def do_move(self, dx, dy):
        for item in self.get_items():
            item.move(dx, dy)
        return self

    def move(self, dx, dy):
        try:
            self.changing()
            self.do_move(dx, dy)
        finally:
            self.change()
        return self

class Group(CompoundWidget):
    def do_set_items(self, items):
        if self.is_mw_displayed():
            self.destroy_items_mw_values()
        super().do_set_items(items)
        if self.is_mw_displayed():
            self.create_items_mw_values(self.get_mw_window())
        return self

    # micro widget
    def create_mw_values(self, mw_window):
        super().create_mw_values(mw_window)
        self.create_items_mw_values(mw_window)
        return self

    def create_items_mw_values(self, mw_window):
        for item in self.get_items():
            item.create_mw_values(mw_window)
        return self
    
    def destroy_mw_values(self):
        super().destroy_mw_values()
        self.destroy_items_mw_values()
        return self

    def destroy_items_mw_values(self):
        for item in self.get_items():
            item.destroy_mw_values()
        return self

"""
class MyWindow(Window):
    def ev_change(self, sender):
        # traceback.print_stack()
        print("change", sender)

    def ev_button_clicked(self, sender, button):
        print("clicked", button)
            
w = MyWindow()
l = Label().set_text("Rostlina").set_x(10).set_y(10)
e = Entry().set_text("Pavla").set_x(10).set_y(30)
g1 = Group().set_items([l, e])

b = Button().set_text("OK").set_x(10).set_y(60)

ch = Checkbox().move(10, 100)

r = Radiobutton().move(40, 100)

g2 = Group().set_items([g1, b, ch, r])

w.set_widget(g2)
"""
