# Vytvoříme třídu Label pro popisky (grafické ovládací prvky)

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



"""
>>> label = Label()
>>> label.get_text()
''
>>> label.set_text("Ahoj")
<__main__.Label object at 0x1037d1d90>
>>> label.get_text()
'Ahoj'
>>> label.set_text(1)
TypeError: text of a label should be a string
"""


