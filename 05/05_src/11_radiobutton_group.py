# Funkční reakce na změnu přepínačů ve skupině.
from omw import *

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

    def deselect_others(self, radiobutton):
        for item in self.get_items():
            if item != radiobutton:
                item.set_value(False)
        return self

    def ev_change(self, sender):
        super().ev_change(sender)
        if sender.is_selected():
            self.deselect_others(sender)

window = Window()
radio1 = Radiobutton()
radio2 = Radiobutton().move(0, 20)
group = RadiobuttonGroup().set_items([radio1, radio2])
window.set_widget(group)

# Můžeme měnit i programově:
"""
>>> radio1.set_value(True)
<omw.Radiobutton object at 0x105e4d310>
>>> radio2.set_value(True)
<omw.Radiobutton object at 0x106042410>
"""

window.main_loop()