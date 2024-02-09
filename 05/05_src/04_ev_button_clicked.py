# Dvě tlačítka s nezávislým chováním
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
button1 = LabeledButton()
button2 = LabeledButton().move(150, 0)
buttons = Group().set_items([button1, button2])
window.set_widget(buttons)
window.main_loop()