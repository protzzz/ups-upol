# Přidáme obsluhy zprávy move popiskům a skupinám.

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
        if type(text) != str:
            raise TypeError("text of a label should be a string")
        self.text = text
        return self

    def move(self, dx, dy):
        self.set_x(self.get_x() + dx)
        self.set_y(self.get_y() + dy)
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

    def move(self, dx, dy):
        for item in self.get_items():
            item.move(dx, dy)
        return self


"""
>>> label = Label()
>>> label.move(10, 20)
<__main__.Label object at 0x10f3bcb90>
>>> print(label.get_x(), label.get_y())
10 20
>>> label2 = Label()
>>> group = Group().set_items([label, label2])
>>> group.move(5, 10)
<__main__.Group object at 0x10f906f50>
>>> print(label.get_x(), label.get_y())
15 30
>>> print(label2.get_x(), label2.get_y())
5 10
"""


