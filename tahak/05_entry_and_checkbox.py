# Textové a zaškrtávací pole

class AtomicWidget:
    def __init__(self):
        self.x = 0
        self.y = 0

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

class Entry(AtomicWidget):
    def __init__(self):
        super().__init__()
        self.text = ""

    def get_text(self):
        return self.text
    
    def set_text(self, text):     
        self.text = text
        return self

class Checkbox(AtomicWidget):
    def __init__(self):
        super().__init__()
        self.value = False

    def get_value(self):
        return self.value
    
    def set_value(self, value):     
        self.value = value
        return self

"""
>>> entry = Entry()
>>> entry.set_x(5)
<__main__.Entry object at 0x10a463a10>
>>> entry.get_x()
5
>>> checkbox = Checkbox()
>>> checkbox.set_x(5)
<__main__.Checkbox object at 0x10a9bbe50>
>>> checkbox.get_x()
5
"""
# Vestavěný predikát isinstance rozhoduje,
# zda je objekt instancí zadané třídy.
"""
>>> isinstance(checkbox, AtomicWidget)
True
>>> isinstance(entry, AtomicWidget)
True
"""
