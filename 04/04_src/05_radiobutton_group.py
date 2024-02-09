# Skupina přepínačů (dvě metody se stejným jménem)


# Stačí prázdná definice:
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
    def __init__(self):
        super().__init__()

    def set_items(self, items):
        for item in items:
            if not isinstance(item, RadioButton):
                raise TypeError("item is not a radiobuton")
        self.items = items[:] 
        return self        
    

"""
>>> rb_group = RadiobuttonGroup()
"""

# Jaká metoda obslouží zprávu?
"""
>>> rb_group.set_items([1, 2])
TypeError: item is not a radiobuton
"""

