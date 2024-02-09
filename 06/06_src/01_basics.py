from proto import obj

# obj je jediný objekt, který máme k dispozici.

"""
>>> obj
<object at 4441084576>
"""

# Objekty se tisknou ve tvaru:
# <název at identifikátor>

# Objektu můžeme zaslat zprávu
# jak jsme zvyklí:
#
# <receiver>.<message>(<arg1>, <arg2>, ...)

# Například název objektu dostaneme zasláním
# zprávy name bez argumentů:
"""
>>> obj.name()
'object'
"""

# Nový objekt vytvoříme zasláním zprávy clone:
"""
>>> point = obj.clone()
>>> point
<object at 4441096048>
"""

# Změnit jméno lze zprávou set_name.
"""
>>> point.set_name("point")
<point at 4441096048>
"""

# Zpráva
#
# <object>.add_slot(<name>)
#
# přidá objektu <object> vlastnost <name>.
#
# Konkrétně obsluhu zpráv
# <name> a set_<name>.
#
# Zpráva <name> zjistí hodnotu
# vlastnosti a zpráva set_<name>
# ji nastaví.
#
# Zpráva na získání hodnoty vlastnosti
# tedy nezačíná předponou get_.
#
# Po vytvoření je hodnota
# vlastnosti None.

"""
>>> point.add_slot("x")
<point at 4441096048>
>>> point.x()
>>> point.set_x(3)
<point at 4441096048>
>>> point.x()
3
"""
