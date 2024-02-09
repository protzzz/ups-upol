# Nefunkční reakce na změnu přepínačů ve skupině. 
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

    def ev_change(self, sender):
        super().ev_change(sender)
        # Nebude fungovat:
        self.set_selected(sender)

window = Window()
radio1 = Radiobutton()
radio2 = Radiobutton().move(0, 20)
group = RadiobuttonGroup().set_items([radio1, radio2])
window.set_widget(group)
window.main_loop()