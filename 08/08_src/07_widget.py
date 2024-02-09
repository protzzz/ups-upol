# Základ funkcionálního uživatelského rozhraní.
from fmw import *

# Funkce label, button a entry očekávají řetězec
# a vrací příslušný prvek uživatelského rozhraní se zadaným textem.
#
# Prvky uživatelského rozhraní se tiskou jako výrazy,
# které když vyhodnotíme, dostaneme opět tištěný tvar.
#
# Například:
"""
>>> label("Jméno:")
label('Jméno:')
>>> button("Stiskni mě")
button('Stiskni mě')
>>> entry("")                                        
entry('')
"""

# Podobně funkce checkbox a radiobutton očekávají
# logickou hodnotu a vrací zaškrtávací pole a přepínač.
# Logická hodnota určuje, zda je prvek vybraný.
#
# Například:
"""
>>> checkbox(True)                                        
checkbox(True)
>>> radiobutton(False)                                        
radiobutton(False)
"""

# Funkce display_window očekává tvar
# a zobrazí okno se zadaným tvarem.
# Funkce display_window není čistá funkce - má vedlejší efekt.

# Například:
"""
>>> display_window(button("Stiskni mě"))
"""

# Mimo IDLE použijte místo display_window
# funkci display_window_and_loop.
#
# Například:
"""
>>> display_window_and_loop(button("Stiskni mě"))
"""

# Pro posunutý prvek zavoláme funkci moved,
# která očekává prvek a přírůstky na obou osách.
#
# Například:
"""
>>> moved(button("Stiskni mě"), 20, 30)                                         
moved(button('Stiskni mě'), 20, 30)
>>> display_window(moved(button("Stiskni mě"), 20, 30))
"""

# Funkce group vrací prvek, který se skládá
# ze dvou zadaných prvků.
#
# Například:
"""
>>> group(label("Jméno:"), moved(entry(""), 0, 20))
group(label('Jméno:'), moved(entry(''), 0, 30))
>>> display_window(group(label("Jméno:"), moved(entry(""), 0, 20)))
"""

# Někdy se může hodit prvek empty_widget, který se vůbec nezobrazí.
"""
>>> empty_widget                                         
empty_widget
>>> display_window(empty_widget)
"""
