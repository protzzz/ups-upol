# Změna reprezentace bodu

# Bod je pole ["point", x, y].

def make_point(x, y):
    return ["point", x, y]

def get_point_x(point):
    return point[1]

def get_point_y(point):
    return point[2]

"""
>>> p1 = make_point(3, 4)
>>> p1
['point', 3, 4]
>>> get_point_x(p1)
3
>>> get_point_y(p1)
4
"""

# Proceduru move_point není potřeba měnit

def move_point(point, dx, dy):
    return make_point(get_point_x(point) + dx,
                      get_point_y(point) + dy)

"""
>>> move_point(p1, 1, 2)
['point', 4, 6]
"""
# Typový predikát:
def is_point(value):
    return (type(value) == list
            and len(value) == 3
            and value[0] == "point")

"""
>>> is_point(p1)
True
>>> is_point([3, 4])
False
>>> is_point(3)
False
"""

# Procedura move_point vrací vždy nový bod

"""
>>> p1 = make_point(3, 4)
>>> p1
['point', 3, 4]
>>> p2 = move_point(p1, 1, 2)
>>> p2
['point', 4, 6]
>>> p1
['point', 3, 4]
"""
