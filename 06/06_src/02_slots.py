from proto import obj


# Objekt definuje pojmenované položky
# nazývané sloty.

point = obj.clone()
point.set_name("point")

# Například nyní má objekt point
# ve slotu name hodnotu "point".

# Když objektu zašleme zprávu,
# jejíž jméno se shoduje s názvem slotu,
# pak se vrátí hodnota slotu.

# Například:

"""
>>> point.name()
'point'
"""

# Zpráva
#
# object.set_slot(name, value)
#
# umožňuje nastavit hodnotu slotu.

point.set_slot("x", 3)

"""
>>> point.x()
3
"""

# Hodnota slotu může být i funkce:
def point_y_as_x(call_super, self):
    return self.x()

point.set_slot("y", point_y_as_x)

# Funkci, která je hodnotou slotu, říkáme metoda.
#
# Uvažujme zaslání zprávy:
#
# <receiver>.<message>(<arg1>, <arg2>, ...)
#
# Pokud je hodnotou slotu <message> funkce,
# pak se funkce zavolá s argumenty:
#
# <call_super>, <receiver>, <arg1>, <arg2>, ...
#
# kde hodnotu <call_super> můžete vysvětlíme později.

# Tedy
#
# point.y()
#
# způsobí zavolání funkce point_y_as_x s argumenty call_super a point.
# Proto:
"""
>>> point.y()
3
"""

# Změna slotu x způsobí změnu vlastností x, y.
"""
>>> point.set_slot("x", 4)
<point at 4363070208>
>>> point.x()
4
>>> point.y()
4
"""

# Zpráva
#
# object.print()
#
# vytiskne sloty objektu. Například:
"""
>>> point.print()
Object <point at 4574655344> slots
----------------------------------
parent:	<object at 4574655248>
name:	'point'
x:	4
y:	<function point_y_as_x at 0x10eb3d510>
"""

# Smysl slotu parent vysvětlíme později.

# Zpráva
#
# <object>.add_slot(<name>)
#
# přesněji nastaví objektu
# hodnotu slotu <name> na None
# a hodnotu slotu set_<name> na metodu,
# která mění hodnotu slotu <name>.

"""
>>> point2 = obj.clone()
>>> point2.add_slot("x")
<object at 4552451472>
>>> point2.add_slot("y")
<object at 4552451472>
>>> point2.set_x(3)
<object at 4552451472>
>>> point2.x()
3
>>> point2.set_y(4)
<object at 4552451472>
>>> point2.y()
4
>>> point2.print()
Object <object at 4552451472> slots
-----------------------------------
parent:	<object at 4552446576>
x:	3
set_x:	<function object_add_slot.<locals>.set_value at 0x10f5c71c0>
y:	4
set_y:	<function object_add_slot.<locals>.set_value at 0x10f5c7250>
"""


point3 = obj.clone()

def point3_set_y(call_super, self, val):
    return self.set_slot("y", val)

point3.set_slot("set_y", point3_set_y)
