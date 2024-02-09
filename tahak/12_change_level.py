# Lepší reakce na změnu přepínačů pomocí úrovně změny.
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

    # provedení nastavení přepnutí přepínače
    def do_set_selected(self, radiobutton):
        for item in self.get_items():
            item.set_value(radiobutton == item)
        return self

    # přepnutí s hláčením změn:
    def set_selected(self, radiobutton):
        # Příkaz try zajistí snížení úrovně změny i v případě chyby:
        try:
            self.changing() # Zvýší úroveň změny
            self.do_set_selected(radiobutton)
        finally:
            self.change() # Sníží úroveň změny
        return self

    def ev_change(self, sender):
        super().ev_change(sender)
        
        # Přepínač vybereme, pouze pokud je nulová úroveň změny:
        if sender.is_selected() and self.get_change_level() == 0:
            self.set_selected(sender)

window = Window()
radio1 = Radiobutton()
radio2 = Radiobutton().move(0, 20)
group = RadiobuttonGroup().set_items([radio1, radio2])
window.set_widget(group)

window.main_loop()