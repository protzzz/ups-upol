# Functional Micro Widget verze 2
#
# Malá knihovna funkcionálního uživatelského rozhraní

import micro_widget as mw

# Třída Widget
class Widget:
    def mw_render(self, window, old_widget, mw_widget):
        if self.is_same_type(old_widget):
            if self != old_widget:
                self.mw_update(window, old_widget, mw_widget)
            return mw_widget
        else:
            if old_widget:
                old_widget.mw_destroy(mw_widget)
            return self.mw_create(window)

    def is_same_type(self, value):
        return False

    def __eq__(self, value):
        return self.is_same_type(value)

# Třída AtomicWidget
class AtomicWidget(Widget):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def mw_update(self, window, old_widget, mw_widget):          
        if old_widget.get_x() != self.get_x():
            mw.set_widget_x(mw_widget, self.get_x())

        if old_widget.get_y() != self.get_y():
            mw.set_widget_y(mw_widget, self.get_y())

    def mw_destroy(self, mw_widget):
        mw.destroy_widget(mw_widget)

    def __eq__(self, value):
        return (super().__eq__(value)
                and self.get_x() == value.get_x()
                and self.get_y() == value.get_y())

    def action_changed(self, change):
        return self

# Třída TextedWidget
class TextedWidget(AtomicWidget):
    def __init__(self, text="", x=0, y=0):
        super().__init__(x, y)
        self.text = text

    def get_text(self):
        return self.text

    def __eq__(self, value):
        return (super().__eq__(value)
                and self.get_text() == value.get_text())

# Třída Label
class Label(TextedWidget):
    def __repr__(self):
        text = self.get_text()
        x = self.get_x()
        y = self.get_y()
        return f"label({repr(text)}, {x}, {y})"

    def is_same_type(self, value):
        return isinstance(value, Label)

    def mw_update(self, window, old_widget, mw_widget):
        if old_widget.get_text() != self.get_text():
            mw.set_button_text(mw_widget, self.get_text())
        super().mw_update(window, old_widget, mw_widget)
            
    def mw_create(self, window):
        mw_window = window.get_mw_window()
        mw_widget = mw.make_label(mw_window)
        self.mw_update(window, label(""), mw_widget)
        return mw_widget

    def moved(self, dx, dy):
        text = self.get_text()
        x = self.get_x()
        y = self.get_y()
        return label(text, x + dx, y + dy)

# Prvek label
label = Label

# Třída Entry
class Entry(TextedWidget):
    def __init__(self, text="", action=None, x=0, y=0):
        super().__init__(text, x, y)
        self.action = action

    def get_action(self):
        return self.action   
        
    def __repr__(self):
        text = self.get_text()
        action = self.get_action()
        x = self.get_x()
        y = self.get_y()
        return f"entry({repr(text)}, {repr(action)}, {x}, {y})"

    def is_same_type(self, value):
        return isinstance(value, Entry)
        
    def mw_update(self, window, old_widget, mw_widget):
        if (old_widget.get_action() != self.get_action()
            or old_widget.get_text() != self.get_text()):
            
            action = self.get_action()
            if action != None:
                def command():
                    text = mw.get_entry_text(mw_widget)
                    mw.set_entry_text(mw_widget, self.get_text())
                    window.process_action([action, text])
                mw.set_entry_command(mw_widget, command)
            else:
                self.mw_set_none_command(mw_widget)

            mw.set_entry_text(mw_widget, self.get_text())
            
            
        super().mw_update(window, old_widget, mw_widget)

    def mw_set_none_command(self, mw_widget):
        def command():
            mw.set_entry_text(mw_widget, self.get_text())
        mw.set_entry_command(mw_widget, command)
        
    def mw_create(self, window):
        mw_window = window.get_mw_window()
        mw_widget = mw.make_entry(mw_window)
        self.mw_set_none_command(mw_widget)
        self.mw_update(window, entry(), mw_widget)
        return mw_widget

    def __eq__(self, value):
        return (super().__eq__(value)
                and self.get_action() == value.get_action())

    def moved(self, dx, dy):
        text = self.get_text()
        action = self.get_action()
        x = self.get_x()
        y = self.get_y()
        return entry(text, action, x + dx, y + dy)

    def action_changed(self, change):
        action = self.get_action()
        if action:
            text = self.get_text()
            x = self.get_x()
            y = self.get_y()
            return entry(text, change(action), x, y)
        else:
            return self

# Prvek entry
entry = Entry

# Třída Button
class Button(TextedWidget):
    def __init__(self, text="", action=None, x=0, y=0):
        super().__init__(text, x, y)
        self.action = action

    def get_action(self):
        return self.action        
    
    def __repr__(self):
        text = self.get_text()
        action = self.get_action()
        x = self.get_x()
        y = self.get_y()
        return f"button({repr(text)}, {repr(action)}, {x}, {y})"

    def is_same_type(self, value):
        return isinstance(value, Button)
        
    def mw_update(self, window, old_widget, mw_widget):
        if old_widget.get_text() != self.get_text():
            mw.set_button_text(mw_widget, self.get_text())

        if old_widget.get_action() != self.get_action():
            action = self.get_action()
            command = (lambda: window.process_action(action)
                       if action != None
                       else lambda: None) 
            mw.set_button_command(mw_widget, command)

        super().mw_update(window, old_widget, mw_widget)
            
    def mw_create(self, window):
        mw_window = window.get_mw_window()
        mw_widget = mw.make_button(mw_window)
        self.mw_update(window, button(""), mw_widget)
        return mw_widget

    def __eq__(self, value):
        return (super().__eq__(value)
                and self.get_action() == value.get_action())

    def moved(self, dx, dy):
        text = self.get_text()
        action = self.get_action()
        x = self.get_x()
        y = self.get_y()
        return button(text, action, x + dx, y + dy)

    def action_changed(self, change):
        action = self.get_action()
        if action:
            text = self.get_text()
            x = self.get_x()
            y = self.get_y()
            return button(text, change(action), x, y)
        else:
            return self

# Prvek button
button = Button

# Třída Selectable
class Selectable(AtomicWidget):
    def __init__(self, value=False, action=None, x=0, y=0):
        super().__init__(x, y)
        self.value = value
        self.action = action

    def get_value(self):
        return self.value

    def get_action(self):
        return self.action

    def __eq__(self, value):
        return (super().__eq__(value)
                and self.get_value() == value.get_value()
                and self.get_action() == value.get_action())

# Třída Checkbox
class Checkbox(Selectable):
    def __repr__(self):
        value = self.get_value()
        action = self.get_action()
        x = self.get_x()
        y = self.get_y()
        return f"checkbox({value}, {repr(action)}, {x}, {y})"

    def is_same_type(self, value):
        return isinstance(value, Checkbox)

    def mw_update(self, window, old_widget, mw_widget):
        if (old_widget.get_value() != self.get_value()
            or old_widget.get_action() != self.get_action()):
            
            action = self.get_action()
            if action != None:
                def command():
                    value = mw.get_checkbox_value(mw_widget)
                    mw.set_radiobutton_value(mw_widget, self.get_value())
                    window.process_action([action, value])
                mw.set_checkbox_command(mw_widget, command)
            else:
                self.mw_set_none_command(mw_widget)

            mw.set_checkbox_value(mw_widget, self.get_value())
            
        super().mw_update(window, old_widget, mw_widget)

    def mw_set_none_command(self, mw_widget):
        def command():
            mw.set_radiobutton_value(mw_widget, self.get_value())
        mw.set_checkbox_command(mw_widget, command)
            
    def mw_create(self, window):
        mw_window = window.get_mw_window()
        mw_widget = mw.make_checkbox(mw_window)
        self.mw_set_none_command(mw_widget)
        self.mw_update(window, checkbox(), mw_widget)
        return mw_widget

    def moved(self, dx, dy):
        value = self.get_value()
        action = self.get_action()
        x = self.get_x()
        y = self.get_y()
        return checkbox(value, action, x + dx, y + dy)

    def action_changed(self, change):
        action = self.get_action()
        if action:
            value = self.get_value()
            x = self.get_x()
            y = self.get_y()
            return checkbox(value, change(action), x, y)
        else:
            return self
        
# Prvek checkbox
checkbox = Checkbox

# Třída Radiobutton
class Radiobutton(Selectable):
    def __repr__(self):
        value = self.get_value()
        action = self.get_action()
        x = self.get_x()
        y = self.get_y()
        return f"radiobutton({value}, {repr(action)}, {x}, {y})"
    
    def is_same_type(self, value):
        return isinstance(value, Radiobutton)
    
    def mw_update(self, window, old_widget, mw_widget):
        if (old_widget.get_value() != self.get_value()
            or old_widget.get_action() != self.get_action()):
            action = self.get_action()
            if action != None:
                def command():
                    value = mw.get_radiobutton_value(mw_widget)
                    mw.set_radiobutton_value(mw_widget, self.get_value())
                    window.process_action([action, value])
                mw.set_radiobutton_command(mw_widget, command)
            else:
                self.mw_set_none_command(mw_widget)

            mw.set_radiobutton_value(mw_widget, self.get_value())
            

        super().mw_update(window, old_widget, mw_widget)

    def mw_set_none_command(self, mw_widget):
        def command():
            mw.set_radiobutton_value(mw_widget, self.get_value())
        mw.set_radiobutton_command(mw_widget, command)
        
    def mw_create(self, window):
        mw_window = window.get_mw_window()
        mw_widget = mw.make_radiobutton(mw_window)
        self.mw_set_none_command(mw_widget)
        self.mw_update(window, radiobutton(), mw_widget)
        return mw_widget

    def moved(self, dx, dy):
        value = self.get_value()
        action = self.get_action()
        x = self.get_x()
        y = self.get_y()
        return radiobutton(value, action, x + dx, y + dy)

    def action_changed(self, change):
        action = self.get_action()
        if action:
            value = self.get_value()
            x = self.get_x()
            y = self.get_y()
            return radiobutton(value, change(action), x, y)
        else:
            return self
        
# Prvek radiobutton
radiobutton = Radiobutton

# Třída Group
class Group(Widget):
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

    def is_same_type(self, value):
        return isinstance(value, Group)
        
    def mw_update(self, window, old_widget, mw_widget):
        self.get_item1().mw_render(window, old_widget.get_item1(), mw_widget[0])
        self.get_item2().mw_render(window, old_widget.get_item2(), mw_widget[1])

    def mw_create(self, window):
        mw_widget1 = self.get_item1().mw_render(window, None, None)
        mw_widget2 = self.get_item2().mw_render(window, None, None)
        return [mw_widget1, mw_widget2]

    def mw_destroy(self, mw_widget):
        self.get_item1().mw_destroy(mw_widget[0])
        self.get_item2().mw_destroy(mw_widget[1])

    def __eq__(self, value):
        return (super().__eq__(value)
                and self.get_item1() == value.get_item1()
                and self.get_item2() == value.get_item2())

    def moved(self, dx, dy):
        return group(self.get_item1().moved(dx, dy),
                     self.get_item2().moved(dx, dy))

    def action_changed(self, change):
        return group(self.get_item1().action_changed(change),
                     self.get_item2().action_changed(change)) 

# Prvek group
group = Group


# Třída EmptyWidget
class EmptyWidget(Widget):
    def __repr__(self):
        return "empty_widget"

    def mw_update(self, window, old_widget, mw_widget):
        pass

    def mw_create(self, window):
        return None

    def mw_destroy(self, mw_widget):
        pass
    
    def is_same_type(self, value):
        return isinstance(value, EmptyWidget)

    def moved(self, dx, dy):
        return self

# Prvek empty_widget
empty_widget = EmptyWidget()


# Prvek moved
def moved(widget, dx, dy):
    return widget.moved(dx, dy)

# Prvek action_changed
def action_changed(widget, change):
    if callable(change):
        change1 = change
    else:
        change1 = lambda a: [change, a]
    return widget.action_changed(change1)
    

# Třída Window
class Window:
    def __init__(self, content, init_state=None, update=None):
        self.content_function = (content
                                 if callable(content)
                                 else lambda state: content)
        self.update_function = update if update else lambda state, action: action
        self.widget = None
        self.mw_widget = None
        self.mw_window = mw.display_window()
        self.ignore_actions = True
        self.set_state(init_state)
        self.ignore_actions = False

    def get_mw_window(self):
        return self.mw_window
        
    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        self.mw_render()
        return self

    def mw_render(self):
        widget = self.content_function(self.state)
        mw_widget = widget.mw_render(self, self.widget, self.mw_widget)
        self.widget = widget
        self.mw_widget = mw_widget
        
    def process_action(self, action):
        if not self.ignore_actions: 
            self.ignore_actions = True
            if action == None:
                new_state = self.get_state()
            else:
                new_state = self.update_function(self.get_state(), action)
            self.set_state(new_state)
            self.ignore_actions = False
        return self

    def main_loop(self):
        mw.main_loop(self.get_mw_window())
        return self
    
# Procedury na zobrazení okna
def display_window(content, init_state=None, update=None):
    Window(content, init_state, update)

def display_window_and_loop(content, init_state=None, update=None):
    Window(content, init_state, update).main_loop()


