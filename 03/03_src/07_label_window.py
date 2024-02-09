# Přidáme ochranu při nastavování vlastnosti widget okna

class Label:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.text = ""
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        if type(x) != int:
            raise TypeError("x coordinate of a label should be an integer")
        self.x = x
        return self
    
    def set_y(self, y):
        if type(y) != int:
            raise TypeError("y coordinate of a label should be an integer")       
        self.y = y
        return self

    def get_text(self):
        return self.text

    def set_text(self, text):
        if not type(text) == str:
            raise TypeError("text of a label should be a string")
        self.text = text
        return self

# Hodnota vlastnosti widget okna musí být None nebo ovládací prvek (widget)
class Window:
    def __init__(self):
        self.widget = None

    def get_widget(self):
        return self.widget

    def set_widget(self, widget):
        if not (widget == None or isinstance(widget, Label)):
            raise TypeError("widget of a window should be None or a widget")
        self.widget = widget
        return self
    
"""
>>> label = Label()
>>> window = Window()
>>> window.set_widget(label)
<__main__.Window object at 0x1038dd550>
>>> window.get_widget()
<__main__.Label object at 0x103519010>
>>> window.set_widget(None)
<__main__.Window object at 0x1038dd550>
>>> window.get_widget()
>>> window.set_widget(1)
TypeError: widget of a window should be None or a widget
"""


