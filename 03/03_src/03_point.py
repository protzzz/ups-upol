# Nastavíme výchozí hodnoty vlastností x, y na nuly.

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        
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

    def get_r(self):
        x = self.get_x()
        y = self.get_y()
        return (x ** 2 + y ** 2) ** 0.5

# Problém s ochranou konzistence
"""
>>> point = Point()
>>> point.set_x("1")
<__main__.Point object at 0x7f906a3cb9d0>
>>> point.get_x()
'1'
>>> point.get_x() + 5
TypeError: can only concatenate str (not "int") to str
"""
