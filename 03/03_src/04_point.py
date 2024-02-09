# Přidáme ochranu při nastavování vlastností x, y.

# vestavěná funkce type
"""
>>> type(1)
<class 'int'>
"""

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        if type(x) != int:
            raise TypeError("x coordinate of a point should be an integer")
        self.x = x
        return self
    
    def set_y(self, y):
        if type(y) != int:
            raise TypeError("y coordinate of a point should be an integer")       
        self.y = y
        return self

    def get_r(self):
        x = self.get_x()
        y = self.get_y()
        return (x ** 2 + y ** 2) ** 0.5


# Ochrana konzistence bodu.
"""
>>> point = Point()
>>> point.x
0
>>> point.set_x(1)
<__main__.Point object at 0x7fd0c62f8100>
>>> point.get_x()
1
>>> point.set_x("1")
TypeError: x coordinate of a point should be an integer
>>> point.get_x()
1
"""

# Chyba způsobená přímým přístupem k atributům objektu.
"""
>>> point = Point()
>>> point.x = "1"
>>> point.get_x() + 5
TypeError: can only concatenate str (not "int") to str
"""

# Obcházení principu zapouzdření:
"""
>>> point = Point()
>>> point.x
0
>>> point.x = 1
"""

# Respektování principu zapouzdření:
"""
>>> point = Point()
>>> point.get_x()
0
>>> point.set_x(1)
<__main__.Point object at 0x7fce023dd9a0>
"""


