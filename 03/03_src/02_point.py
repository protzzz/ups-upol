# Bodům přidáme vlastnosti x, y

class Point:
    def __init__(self):
        self.x = None
        self.y = None
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        self.x = x
        return self
    
    def set_y(self, y):
        self.y = y
        return self

    # metoda na výpočet vzdálenosti od počátku
    def get_r(self):
        x = self.get_x()
        y = self.get_y()
        return (x ** 2 + y ** 2) ** 0.5

"""
>>> point = Point()
>>> point.get_x()
>>> point.set_x(3)
<__main__.Point object at 0x10afcbc10>
>>> point.get_x()
3
>>> point.set_y(4)
<__main__.Point object at 0x10afcbc10>
>>> point.get_r()
5.0
"""
