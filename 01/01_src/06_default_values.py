# Výchozí hodnoty položek
# Bod má po vytvoření souřadnice [0, 0].

def make_point():
    return ["point", 0, 0]

def get_point_x(point):
    return point[1]

def get_point_y(point):
    return point[2]

def set_point_x(point, x):
    point[1] = x

def set_point_y(point, y):
    point[2] = y


def move_point(point, dx, dy):
    set_point_x(point, get_point_x(point) + dx)
    set_point_y(point, get_point_y(point) + dy)

"""
>>> p1 = make_point()
>>> p1
['point', 0, 0]
>>> move_point(p1, 3, 4)
>>> p1
['point', 3, 4]
"""

