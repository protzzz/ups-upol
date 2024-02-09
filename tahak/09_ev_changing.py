# Událost ev_changing se zasílá před chystanou změnou.
# Skupina zaškrtávacích tlačítek tiskne hodnoty před a po změně.
from omw import *

class CheckboxGroup(Group):
    def print_values(self):
        for item in self.get_items():
            print(item.get_value(), end=" ")
        print()
            
    def ev_changing(self, sender):
        super().ev_change(sender)
        print("Před změnou:")
        self.print_values()
        print()
        
    def ev_change(self, sender):
        super().ev_change(sender)
        print("Po změně:")
        self.print_values()
        print()
    

window = Window()
checkbox1 = Checkbox()
checkbox2 = Checkbox().move(0, 30)
group = CheckboxGroup().set_items([checkbox1, checkbox2])
window.set_widget(group)

"""
checkbox1.set_value(False)
"""

window.main_loop()