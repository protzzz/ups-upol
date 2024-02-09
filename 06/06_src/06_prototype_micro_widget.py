# Uživatelské rozhraní pomocí knihovny Prototyp Micro Widget
from pmw import *

# Vytvoření nového okna:
window1 = window.clone()

# Zobrazení okna:
window1.display()

# Přidání popisku:
label1 = label.clone().set_text("Jméno:")
window1.set_widget(label1)

# Přidání textového pole:
entry1 = entry.clone().move(0, 20)
group1 = group.clone().set_items([label1, entry1])
window1.set_widget(group1)

# Zjištění zadaného texu:
"""
>>> entry1.text()
'Petr'
"""

# Přidání obsluhy události na změnu textu v poli:
def window1_ev_entry_text_change(call_super, self, entry):
    print("Změna textu v poli:", entry, entry.text())

window1.set_slot("ev_entry_text_change", window1_ev_entry_text_change)

# Po zadání "Petr" do textového pole se vytiskne:
"""
Změna textu v poli: <entry at 4498149264> P
Změna textu v poli: <entry at 4498149264> Pe
Změna textu v poli: <entry at 4498149264> Pet
Změna textu v poli: <entry at 4498149264> Petr
"""

# Přidání tlačítka:
button1 = button.clone().set_text("Odešli").move(0, 50)
group1.set_items([label1, entry1, button1])

# Přidání obsluhy události na kliknutí na tlačítko:
def window1_ev_button_clicked(call_super, self, button):
    print("Kliknuto na tlačítko:", button)

window1.set_slot("ev_button_clicked", window1_ev_button_clicked)

# Po kliknutí na tlačítko se vytiskne:
"""
Kliknuto na tlačítko: <button at 4439566416>
"""

# Odeslání textu v poli:
def group1_ev_button_clicked2(call_super, self, button):
    text = self.items()[1].text()
    print("Jméno uživatele:", text)

group1.set_slot("ev_button_clicked", group1_ev_button_clicked2)
# Po zadání "Petr" a kliku na "Odešli" se vytiskne:
"""
Jméno uživatele: Petr
"""

# Okno window1 můžeme naklonovat:
"""
>>> window2 = window1.clone()
>>> window2.display()
<window at 4554439184>
"""

# Při změně prototypu musíme nechat znovu zobrazit obsah okna.
"""
entry1.set_text("A")
Změna textu v poli: <entry at 4545625232> A
<entry at 4545625232>
window2.redisplay()
"""
    
