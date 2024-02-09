# Přehled základních procedur knihovny micro_widget

import micro_widget as mw

# Zobrazení okna
w = mw.display_window()
"""

# Přidání popisku
"""
l = mw.make_label(w)
mw.set_label_text(l, "Borůvka")
mw.set_widget_x(l, 20)
mw.set_widget_y(l, 10)
"""

# Změna
"""
mw.set_label_text(l, "Jahoda")
mw.set_widget_y(l, 20)
"""

# Přidání tlačítka
"""
b = mw.make_button(w)
mw.set_button_text(b, "Stiskni mě!")
mw.set_widget_x(b, 20)
mw.set_widget_y(b, 40)
"""

# Nastavení příkazu tlačítka
"""
def print_command():
    print("Stiskl jsi tlačítko")


mw.set_button_command(b, print_command)
"""

"""
# Tlačítko změní text popisku
"""
def set_label_text_command():
    mw.set_label_text(l, "Banán")

mw.set_button_command(b, set_label_text_command)    
"""

# Přidání textového pole
"""
e = mw.make_entry(w)
mw.set_widget_x(e, 20)
mw.set_widget_y(e, 70)
"""

# Stisk tlačítka změní text popisku podle textu v poli
"""
def copy_entry_text_command():
    mw.set_label_text(l, mw.get_entry_text(e))

mw.set_button_command(b, copy_entry_text_command)  
"""

# Nastavení příkazu textového pole
"""
mw.set_entry_command(e, copy_entry_text_command)
"""


# Odstranění tlačítka
"""
mw.destroy_widget(b)
"""

