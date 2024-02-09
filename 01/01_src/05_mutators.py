# Mutátory bodu

def make_point(x, y):
    return ["point", x, y]

def get_point_x(point):
    return point[1]

def get_point_y(point):
    return point[2]

def set_point_x(point, x):
    point[1] = x

def set_point_y(point, y):
    point[2] = y


"""
>>> p1 = make_point(3, 4)
>>> p1
['point', 3, 4]
>>> set_point_x(p1, 5)
>>> p1
['point', 5, 4]
>>> p2 = p1
>>> set_point_y(p1, 3)
>>> p1
['point', 5, 3]
>>> p2
['point', 5, 3]
"""

# Destruktivní posun bodu
def move_point(point, dx, dy):
    set_point_x(point, get_point_x(point) + dx)
    set_point_y(point, get_point_y(point) + dy)

"""
>>> p1 = make_point(3, 4)
>>> move_point(p1, 1, 2)
>>> p1
['point', 4, 6]
"""

