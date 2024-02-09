from proto import obj

# Zpráva
#
# <object>.clone()
#
# vytvoří nový objekt s jediným slotem
# parent, jehož hodnota bude <object>.

point = obj.clone()

"""
>>> point.print()
Object <object at 4531008224> slots
-----------------------------------
parent:	<object at 4531008128>
"""

# Hodnota slotu parent se jmenuje rodič.

# Pokud objektu zašleme zprávu message
# a on nemá slot stejného jména, ale
# má rodiče, pak se obsluha zprávy
# bude hledat v rodiči.


# Například:
"""
>>> point.add_slot("x")
<object at 4531008224>
>>> point.set_x(3)
<object at 4531008224>
>>> p1 = point.clone()
>>> p1.x()
3
"""

# Objekty mají sloty:
"""
>>> p1.print()
Object <object at 4531005584> slots
-----------------------------------
parent:	<object at 4531008224>


>>> point.print()
Object <object at 4531008224> slots
-----------------------------------
parent:	<object at 4531008128>
x:	3
set_x:	<function object_add_slot.<locals>.set_value at 0x10e1875b0>
"""

# Tedy při zaslání zprávy:
#
# p1.x()
#
# se nejprve hledal slot x
# v objektu p1. Tam se nenašel,
# tak hledání pokračovalo u jeho rodiče
# objektu point, kde slot x má hodnotu 3.
# Proto číslo 3 je obsluhou zprávy x
# zaslanou objektu p1.

# Pokud objektu p1 zašleme zprávu set_x,
# pak se obsluha najde v objektu point.
#
# Obsluhou je metoda, která se zavolá.
# Přestože se obsluha našla v objektu point,
# druhý argument volaní metody bude příjemce zprávy,
# tedy objekt p1.
#
# Proto zpráva set_x změní objekt p1
# a ne objekt point:

"""
>>> p1.set_x(4)
<object at 4467440080>
>>> p1.x()
4
>>> p1.print()
Object <object at 4467440080> slots
-----------------------------------
parent:	<object at 4467438304>
x:	4

<object at 4467440080>
>>> point.print()
Object <object at 4467438304> slots
-----------------------------------
parent:	<object at 4467438208>
x:	3
set_x:	<function object_add_slot.<locals>.set_value at 0x10a4e70a0>

<object at 4467438304>
"""
