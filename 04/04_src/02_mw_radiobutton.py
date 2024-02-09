# Přepínač v micro_widget verze 2
import micro_widget as mw

# vytvoříme okno
window = mw.display_window()

# přidáme dva přepínače
radiobutton1 = mw.make_radiobutton(window)
mw.set_widget_x(radiobutton1, 20)
mw.set_widget_y(radiobutton1, 20)

radiobutton2 = mw.make_radiobutton(window)
mw.set_widget_x(radiobutton2, 20)
mw.set_widget_y(radiobutton2, 40)

# popisky
label1 = mw.make_label(window)
mw.set_label_text(label1, "černá")
mw.set_widget_x(label1, 40)
mw.set_widget_y(label1, 20)

label2 = mw.make_label(window)
mw.set_label_text(label2, "červená")
mw.set_widget_x(label2, 40)
mw.set_widget_y(label2, 40)


# zajistíme, aby byl vybrán nejvíše jeden přepínač

def radiobutton1_command():
    print("Změna prvního přepínače", mw.get_radiobutton_value(radiobutton1))
    if mw.is_radiobutton_selected(radiobutton1):
        mw.set_radiobutton_value(radiobutton2, False)

def radiobutton2_command():
    print("Změna druhého přepínače", mw.get_radiobutton_value(radiobutton2))
    if mw.is_radiobutton_selected(radiobutton2):
        mw.set_radiobutton_value(radiobutton1, False)
"""
mw.set_radiobutton_command(radiobutton1, radiobutton1_command)
mw.set_radiobutton_command(radiobutton2, radiobutton2_command)
"""
