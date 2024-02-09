# Skupina přepínačů s knihovnou omw
from omw import *

class Radiobutton():
    pass

class RadiobuttonGroup(Group):
    def check_item(self, item):
        if not isinstance(item, Radiobutton):
            raise TypeError("items of a radiobutton group have to be radiobuttons")
        return self

    def get_selected(self):
        for item in self.get_items():
            if item.is_selected():
                return item

    def set_selected(self, radiobutton):
        for item in self.get_items():
            item.set_value(radiobutton == item)
        return self

    def deselect_all(self):
        for item in self.get_items():
            item.set_value(False)
        return self

w = Window()
r1 = Radiobutton()
r2 = Radiobutton().move(0, 20)
g = RadiobuttonGroup().set_items([r1, r2])
w.set_widget(g)

"""
>>> r1
<omw.Radiobutton object at 0x10b512dd0>
>>> r2
<omw.Radiobutton object at 0x10b5fa3d0>
>>> g.get_selected()
>>> g.set_selected(r1)
<__main__.RadiobuttonGroup object at 0x10b5fa390>
>>> g.get_selected()
<omw.Radiobutton object at 0x10b512dd0>
>>> g.set_selected(r2)
<__main__.RadiobuttonGroup object at 0x10b5fa390>
>>> g.get_selected()
<omw.Radiobutton object at 0x10b5fa3d0>
>>> g.deselect_all()
<__main__.RadiobuttonGroup object at 0x10b5fa390>
>>> g.get_selected()
"""
# Zatím nefunguje přepínání kliknutím.
