# Textové a zaškrtávací pole
#
# (Pro jednoduchost je odstraněna kontrola
# hodnot vlastností.)

class Entry:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.text = ""
        
    def get_x(self):
        return self.x
    
    def set_x(self, x):
        self.x = x
        return self
    
    def get_y(self):
        return self.y
    
    def set_y(self, y):     
        self.y = y
        return self

    def get_text(self):
        return self.text
    
    def set_text(self, text):     
        self.text = text
        return self

class Checkbox:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.value = False
        
    def get_x(self):
        return self.x
    
    def set_x(self, x):
        self.x = x
        return self
    
    def get_y(self):
        return self.y
    
    def set_y(self, y):     
        self.y = y
        return self

    def get_value(self):
        return self.value
    
    def set_value(self, value):     
        self.value = value
        return self

# Obě třídy definují atributy x, y
# a vlastnosti x, y.
#
# Například:
"""
>>> entry = Entry()
>>> entry.set_x(5)
<__main__.Entry object at 0x10b24ba10>
>>> entry.get_x()
5
>>> checkbox = Checkbox()
>>> checkbox.set_x(5)
<__main__.Checkbox object at 0x10b7a3e50>
>>> checkbox.get_x()
5
"""

# Liší se v tom, že textové pole má vlastnost text
# a zaškrtávací pole vlastnost value.
"""
>>> entry.set_text("A")
<__main__.Entry object at 0x10b24ba10>
>>> entry.get_text()
'A'
>>> checkbox.set_value(True)
<__main__.Checkbox object at 0x10b7a3e50>
>>> checkbox.get_value()
True
"""
