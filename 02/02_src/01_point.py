# Opakování: datová struktura bod

def make_point(x, y):
    return [x, y]

def get_point_x(point):
    return point[0]

def get_point_y(point):
    return point[1]

def set_point_x(point, x):
    point[0] = x

def set_point_y(point, y):
    point[1] = y


"""
>>> point = make_point(3, 4)
>>> get_point_x(point)
3
>>> set_point_x(point, 5)
>>> get_point_x(point)
5
"""

