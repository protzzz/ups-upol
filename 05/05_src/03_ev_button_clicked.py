# Událost ev_button_clicked se zašle při kliku na tlačítko.
from omw import *

class LabeledButton(Group):
    def __init__(self):
        super().__init__()
        button = Button().set_text("Klikni na mě!")
        label = Label().move(0, 30)
        self.set_items([button, label])

    def get_label(self):
        return self.get_items()[1]
    
    def display_text(self):
        self.get_label().set_text("Kliknuto na tlačítko")
        return self
        
    def ev_button_clicked(self, sender, button):
        super().ev_button_clicked(sender, button)
        self.display_text()
    
window = Window()
labeled_button = LabeledButton()
window.set_widget(labeled_button)
window.main_loop()