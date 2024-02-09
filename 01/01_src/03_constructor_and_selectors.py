# Konstruktor a selektory
import os

def clear():
    os.system('printf "\033c"')

def make_point(x, y):
    return [x, y]

"""
>>> p1 = make_point(3, 4)
"""

def get_point_x(point):
    return point[0]

def get_point_y(point):
    return point[1]

"""
>>> get_point_x(p1)
3
>>> get_point_y(p1)
4
"""

def move_point(point, dx, dy):
    return make_point(get_point_x(point) + dx,
                      get_point_y(point) + dy)

"""
>>> move_point(p1, 1, 2)
[4, 6]
"""

# Procedura move_point vrací vždy nový bod:
"""
>>> p1
[3, 4]
>>> p2 = move_point(p1, 1, 2)
>>> p2
[4, 6]
>>> p1
[3, 4]
"""
