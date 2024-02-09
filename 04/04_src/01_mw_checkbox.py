# Zaškrtávací pole v micro_widget verze 2
import micro_widget as mw

# vytvoříme okno
window = mw.display_window()

# přidáme zaškrtávací pole
checkbox = mw.make_checkbox(window)
mw.set_widget_x(checkbox, 20)
mw.set_widget_y(checkbox, 20)

# změna hodnoty
mw.set_checkbox_value(checkbox, True)

# popisek není součástí zaškrtávacího pole
label = mw.make_label(window)
mw.set_label_text(label, "Připraven?")
mw.set_widget_x(label, 40)
mw.set_widget_y(label, 20)


# přidáme příkaz
def checkbox_command():
    print("Změna:", mw.get_checkbox_value(checkbox))
    if mw.is_checkbox_selected(checkbox):
        print("Zaškrtávací pole vybráno")

mw.set_checkbox_command(checkbox, checkbox_command)

