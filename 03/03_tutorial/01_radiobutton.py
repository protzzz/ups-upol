# Přepínač a skupina přepínačů
class Radiobutton:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = False
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        if type(x) != int:
            raise TypeError("x coordinate of a radiobutton should be an integer")
        self.x = x
        return self
    
    def set_y(self, y):
        if type(y) != int:
            raise TypeError("y coordinate of a radiobutton should be an integer")       
        self.y = y
        return self

    def get_state(self):
        return self.state

    def set_state(self, state):
        if type(state) != bool:
            raise TypeError("state of a radiobutton should be a boolean")
        self.state = state
        return self

    def move(self, dx, dy):
        self.set_x(self.get_x() + dx)
        self.set_y(self.get_y() + dy)
        return self

    def toggle(self):
        return self.set_state(not self.get_state())

    def is_selected(self):
        return self.get_state()

"""
>>> r = Radiobutton()
>>> r.get_state()
False
>>> r.toggle().get_state()
True
>>> r.move(20, 30)
<__main__.Radiobutton object at 0x1106bda50>
>>> print(r.get_x(), r.get_y())
20 30
"""

class RadiobuttonGroup:
    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items[:]

    def set_items(self, items):
        for item in items:
            if not isinstance(item, Radiobutton):
                raise TypeError("items of a radiobutton group have to be an array of radiobuttons")
        self.items = items[:] 
        return self

    def add_item(self, item):
        self.set_items(self.get_items() + [item])
        return self
    
    def move(self, dx, dy):
        for item in self.get_items():
            item.move(dx, dy)
        return self

"""
>>> rg = RadiobuttonGroup().set_items([Radiobutton(), Radiobutton().move(0, 20)])
>>> rg.get_items()
[<__main__.Radiobutton object at 0x110823190>, <__main__.Radiobutton object at 0x110823250>]
"""

# Úkol: Zajistit, aby vždy platilo:
#           Ve skupině může být vybrán nejvíše jeden přepínač.
#
# Kroky k řešení:
#  1. Skupině přepínačů přidáme vlastnost selected,
#     jejíž hodnotou je vybraný přepínač.
#     Pokud žádný přepínač není vybrán, vlastnost má hodnotu None.
#     Nastavení hodnoty vlastnosti selected
#     zruší vybrání dříve vybraného přepínače.
#
#  2. Uživatel smí zapínat přepínače pouze nastavením vlastnosti selected.
#
#  3. Po nastavení vlastnosti items zrušit vybrání všech přepínačů.
