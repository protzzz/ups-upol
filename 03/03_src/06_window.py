# Přidáme třídu Window pro okna

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

class Window:
    def __init__(self):
        self.widget = None

    def get_widget(self):
        return self.widget

    def set_widget(self, widget):
        # Ochrana?
        self.widget = widget
        return self

# Vestavěná funkce isinstance rozhoduje,
# zda je hodnota přímou instancí třídy.

"""
>>> label = Label()
>>> isinstance(label, Label)
True
>>> isinstance(label, Window)
False
>>> window = Window()
>>> window.set_widget(label)
>>> isinstance(window.get_widget(), Label)
True
"""


