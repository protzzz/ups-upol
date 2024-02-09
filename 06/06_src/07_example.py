# Ukázka použití knihovny Prototyp Micro Widget
from pmw import *

window1 = window.clone()
window1.display()

label1 = label.clone().set_text("A")
button1 = button.clone().move(0, 30).set_text("B")
entry1 = entry.clone().move(0, 60)
checkbox1 = checkbox.clone().move(0, 90)
radiobutton1 = radiobutton.clone().move(40, 90)

group1 = group.clone().set_items([label1, button1, entry1, checkbox1, radiobutton1])
window1.set_widget(group1)

def window1_ev_button_clicked(call_super, self, sender):
    print("Kliknuto na tlačítko:", sender)
    
window1.set_slot("ev_button_clicked", window1_ev_button_clicked)

def window1_ev_entry_text_change(call_super, self, sender):
    print("Změna textového pole:", sender)
    
window1.set_slot("ev_entry_text_change", window1_ev_entry_text_change)

def window1_ev_checkbox_value_change(call_super, self, sender):
    print("Změna zaškrtávacího pole:", sender)
    
window1.set_slot("ev_checkbox_value_change", window1_ev_checkbox_value_change)

def window1_ev_radiobutton_value_change(call_super, self, sender):
    print("Změna přepínače:", sender)
    
window1.set_slot("ev_radiobutton_value_change", window1_ev_radiobutton_value_change)
window2 = window1.clone()
window2.display()
