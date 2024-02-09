from pmw import *

# Vytvoříme prototyp labeled_radiobutton pro přepínač s popiskem:
radiobutton1 = radiobutton.clone()
label1 = label.clone().move(30, 0)
labeled_radiobutton = group.clone().set_items([radiobutton1, label1])

def labeled_radiobutton_radiobutton(call_super, self):
    return self.items()[0]

labeled_radiobutton.set_slot("radiobutton", labeled_radiobutton_radiobutton)

def labeled_radiobutton_label(call_super, self):
    return self.items()[1]

labeled_radiobutton.set_slot("label", labeled_radiobutton_label)

# Test:
"""
>>> window1 = window.clone()
>>> l_r1 = labeled_radiobutton.clone()
>>> l_r1.label().set_text("A")
<label at 4353704784>
>>> window1.set_widget(l_r1)
<window at 4352610576>
>>> window1.display()
<window at 4352610576>
>>> l_r1.radiobutton().set_value(True)
<radiobutton at 4353704720>
"""

# Vytvoříme prototyp pro skupinu přepínačů:
radiobutton_group = group.clone()


# Přidáme obsluhu události přepnutí přepínače:
def radiobutton_group_ev_radiobutton_value_change(call_super, self, sender):
    if sender.value():
        for l_r in self.items():
            if l_r.radiobutton() != sender:
                l_r.radiobutton().set_value(False)
    
radiobutton_group.set_slot("ev_radiobutton_value_change",
                           radiobutton_group_ev_radiobutton_value_change)

# Test:
"""
l_r1 = labeled_radiobutton.clone()
l_r1.label().set_text("A")
l_r2 = labeled_radiobutton.clone().move(0, 30)
l_r2.label().set_text("B")

r_g1 = radiobutton_group.clone()
r_g1.set_items([l_r1, l_r2])

window1 = window.clone()
window1.set_widget(r_g1)
window1.display()
"""
