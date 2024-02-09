# Přidáme třídu Point pro body
# Bod má atributy x, y

class Point:
    def __init__(self):
        self.x = None
        self.y = None 

"""
>>> point = Point()
>>> point.x
>>> point.x = 3
>>> point.x
3
>>> point.y = 4
>>> (point.x ** 2 + point.y ** 2) ** 0.5
5.0
"""
