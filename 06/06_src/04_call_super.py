from proto import obj


# prototyp label pro popisky.
# Popisek má vlastnost text.
label = obj.clone()
label.set_name("label")
label.add_slot("text")
label.set_text("")


# prototyp window pro okna
# Okno má vlastnost widget pro obsah okna.
window = obj.clone()
window.set_name("window")
window.add_slot("widget")

# Při klonování okna vzniká problém
# s jeho prvkem:
"""
>>> win1 = window.clone().set_widget(label.clone())
>>> win2 = win1.clone()
>>> win1.widget() is win2.widget()
True
"""
# Vidíme, že obě okna sdílí obsah.
# Změna obsahu win2 tedy způsobí nežadoucí
# změnu obsahu win1:
"""
>>> win2.widget().set_text("A")
<label at 4332273360>
>>> win1.widget().text()
'A'
"""
# Potřebujeme přepsat kolonování okna tak,
# aby naklonovalo i svůj obsah.
#
# Budeme potřebovat umět zavolat přepsanou metodu.
#
# První argument metody call_super je funkce bez parametrů.
# Její zavolání způsobí volání přepsané metody.
#
# V následující metodě tedy nejdříve naklonujeme okno standardně
# a poté mu změníme obsah na klon obsahu klonovaného okna.
# Odkomentujte:
#"""
def window_clone(call_super, self):
    clone = call_super()
    if self.widget():
        clone.set_widget(self.widget().clone())
    return clone

window.set_slot("clone", window_clone)
#"""

# Ověření:
"""
>>> win1 = window.clone().set_widget(label.clone().set_text("A"))
>>> win2 = win1.clone()
>>> win1.widget() is win2.widget()
False
>>> win2.widget().set_text("B")
<label at 4354072080>
>>> win1.widget().text()
''
"""

# Text popisku v okně win1 se nezměnil.
