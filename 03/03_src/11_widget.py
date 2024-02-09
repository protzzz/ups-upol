# Okno a ovládací prvky dohromady

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

    def get_r(self):
        x = self.get_x()
        y = self.get_y()
        return (x ** 2 + y ** 2) ** 0.5

    def get_text(self):
        return self.text

    def set_text(self, text):
        if not type(text) == str:
            raise TypeError("text of a label should be a string")
        self.text = text
        return self

class Group:
    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items[:]

    def set_items(self, items):
        for item in items:
            if not (isinstance(item, Label)
                    or isinstance(item, Group)):
                raise TypeError("items of a group have to be an array of widgets")
        self.items = items[:] 
        return self

class Window:
    def __init__(self):
        self.widget = None

    def get_widget(self):
        return self.widget

    def set_widget(self, widget):
        if not (widget == None
                or isinstance(widget, Label)
                or isinstance(widget, Group)): # museli jsem přidat - nepříjemné
            raise TypeError("widget of a window should be None or a widget")
        self.widget = widget
        return self


"""
>>> label1 = Label().set_text("A")
>>> label2 = Label().set_text("B")
>>> window = Window().set_widget(Group().set_items([label1, label2]))
>>> window.get_widget().get_items()[0]
<__main__.Label object at 0x105799250>
>>> window.get_widget().get_items()[0].get_text()
'A'
"""


