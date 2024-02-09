# Skupina přepínačů (bez inicializační metody)

class RadioButton:
    pass

class Group:
    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items[:]

    def set_items(self, items):
        self.items = items[:] 
        return self

class RadiobuttonGroup(Group):
    def set_items(self, items):
        for item in items:
            if not isinstance(item, RadioButton):
                raise TypeError("item is not a radiobuton")
        super().set_items(items)
        return self        
    

"""
>>> radio1 = RadioButton()
>>> radio2 = RadioButton()
>>> radio_group = RadiobuttonGroup()
>>> radio_group.set_items([radio1, radio2])
<__main__.RadiobuttonGroup object at 0x1040bcf90>
>>> radio_group.get_items()
[<__main__.RadioButton object at 0x103f59a50>, <__main__.RadioButton object at 0x1040bce10>]
"""

