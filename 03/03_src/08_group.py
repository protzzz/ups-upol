# Přidáme třídu Group pro skupiny ovládacích prvků

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

class Group:
    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items

    def set_items(self, items):
        for item in items:
            if not (isinstance(item, Label)
                    or isinstance(item, Group)):
                raise TypeError("items of a group have to be an array of widgets")
        self.items = items
        return self

    
"""
>>> group1 = Group()
>>> label = Label()
>>> group1.set_items([label])
<__main__.Group object at 0x1027b8f90>
>>> group1.get_items()
[<__main__.Label object at 0x102b7d4d0>]
>>> group2 = Group()
>>> group1.set_items([label, group2])
<__main__.Group object at 0x1027b8f90>
>>> group1.get_items()
[<__main__.Label object at 0x102b7d4d0>, <__main__.Group object at 0x102505790>]
>>> group1.set_items([label, 1])
TypeError: items of a group have to be an array of widgets
>>> group1.set_items(1)
TypeError: 'int' object is not iterable
"""

# Problém porušení konzistence skupiny
"""
>>> items = [label]
>>> group1.set_items(items)
<__main__.Group object at 0x1027b8f90>
>>> group1.get_items()
[<__main__.Label object at 0x102b7d4d0>]
>>> items[0] = 1
>>> items
[1]
>>> group1.get_items()
[1]
"""


