from omw import *

DEFAULT = 1

class CheckboxGroup(Group):
    def __init__(self):
        super().__init__()
        checkbox = Checkbox().move(10, 160)
        self.set_items([checkbox])

class ButtonGroup(Group):
    def __init__(self, form):
        super().__init__()
        self.form = form

class RadiobuttonGroup(Group):
    def __init__(self):
        super().__init__()
        radio1 = Radiobutton().move(5, 10)
        radio2 = Radiobutton().move(5, 40)

        self.set_items([radio1, radio2])

    def check_item(self, item):
        if not isinstance(item, Radiobutton):
            raise TypeError("Items of a radiobutton group have to be radiobuttons")
        super().check_item(item) 

    def get_selected(self):
        for item in self.get_items():
            if item.is_selected():
                return item

    def set_selected(self, radiobutton):
        for item in self.get_items():
            item.set_value(radiobutton == item)
        return self

    def deselect_others(self, radiobutton):
        for item in self.get_items():
            if item != radiobutton:
                item.set_value(False)
        return self

    def ev_change(self, sender):
        super().ev_change(sender)
        if sender.is_selected():
            self.deselect_others(sender)

class IntegerEntry(Entry):
    def set_text(self, text):
        if text.isdigit() or text == "":
            super().set_text(text)

    def get_value(self):
        return int(self.get_text())

    def set_value(self, value):
        return self.set_text(str(value))
    
    def is_valid(self):
        return self.get_text().isdecimal()

class IntegerEntryField(Group):
    def init(self):
        super().init()
        label = Label()
        entry1 = IntegerEntry().move(55, 60)
        entry2 = IntegerEntry().move(55, 80)
        validation_label = Label().move(0, 100)
        self.set_items([label, entry1, entry2, validation_label])

    def get_label(self):
        return self.get_items()[0]

    def get_entry_first(self):
        return self.get_items()[1]
    
    def get_entry_second(self):
        return self.get_items()[2]

    def get_validation_label(self):
        return self.get_items()[3]
    
    def validate(self):
        start_value = self.get_entry_first().get_text()
        end_value = self.get_entry_second().get_text()

        if start_value and end_value:
            try:
                start_value = int(start_value)
                end_value = int(end_value)

                if start_value >= end_value or start_value <= 0:
                    self.get_validation_label().set_text("Invalid input. Check your range and make sure it's positive.")
                else:
                    self.get_validation_label().set_text("")
            except ValueError:
                self.get_validation_label().set_text("Invalid input. Please enter valid integers.")
        else:
            self.get_validation_label().set_text("")

    def ev_change(self, sender):
        super().ev_change(sender)
        if isinstance(sender, IntegerEntry):
            self.validate()


class Form(Group):
    def __init__(self, radiobutton_group):
        super().__init__()
        self.radiobutton_group = radiobutton_group

        label1 = Label().set_text("Tisknout všechny stránky").move(25, 10)
        label2 = Label().set_text("Stránky v určitém rozsahu").move(25, 40)
        label3 = Label().set_text("od").move(35, 60)
        label4 = Label().set_text("do").move(35, 80)
        label5 = Label().set_text("Počet kopií:").move(5, 140)
        label6 = Label().set_text(str(DEFAULT)).move(80, 140)
        label7 = Label().set_text("").move(35, 100)
        label8 = Label().set_text("Tisknout oboustranně").move(30, 160)

        entry1 = IntegerEntry().move(55, 60)
        entry2 = IntegerEntry().move(55, 80)

        button1 = Button().set_text("+").move(95, 135)
        button2 = Button().set_text("-").move(195, 135)
        button3 = Button().set_text("TISK!").move(90, 175)

        checkbox = Checkbox().move(10, 160)

        label_group = Group().set_items([label1, label2, label3, label4, label5, label6, label7, label8])
        entry_group = Group().set_items([entry1, entry2])
        button_group = ButtonGroup(self).set_items([button1, button2, button3])
        checkbox_group = CheckboxGroup().set_items([checkbox])

        self.set_items([radiobutton_group, label_group, entry_group, button_group, checkbox_group])

    def get_radiobutton(self):
        return self.radiobutton_group.get_selected()

    def get_labels(self):
        return self.get_items()[1]
    
    def get_entry(self):
        return self.get_items()[2]
    
    def get_button(self):
        return self.get_items()[3]
    
    def get_checkbox(self):
        return self.get_items()[4]

    def validate_entry(self):
        entry1 = self.get_items()[2].get_items()[0].get_value()
        entry2 = self.get_items()[2].get_items()[1].get_value()
        label7 = self.get_items()[1].get_items()[6]

        if not (isinstance(entry1, int) and isinstance(entry2, int)):
            label7.set_text("Invalid input. Please enter integer values.")
        elif entry1 < 0 or entry2 < 0:
            label7.set_text("Invalid input. Values cannot be negative.")
        elif entry1 > entry2:
            label7.set_text("Invalid input. Start value cannot be greater than end value.")
        else:
            label7.set_text("")

    def ev_change(self, sender):
        super().ev_change(sender)
        if sender in [self.get_items()[2].get_items()[0], self.get_items()[2].get_items()[1]]:
            self.validate_entry()

    def inc_counter(self):
        label6 = self.get_items()[1].get_items()[-3]
        current_value = int(label6.get_text())
        new_value = current_value + 1
        label6.set_text(str(new_value))

    def dec_counter(self):
        label6 = self.get_items()[1].get_items()[-3]
        current_value = int(label6.get_text())
        new_value = max(1, current_value - 1)
        label6.set_text(str(new_value))

    def ev_button_clicked(self, sender, button):
        super().ev_button_clicked(sender, button)
        if button.get_text() == "+":
            self.inc_counter()
        elif button.get_text() == "-":
            self.dec_counter()
        elif button.get_text() == "TISK!":
            selected_radiobutton = self.get_radiobutton()
            pocet = int(self.get_items()[1].get_items()[-3].get_text())
            is_double = self.get_items()[-1].get_items()[0].is_selected()

            if selected_radiobutton == self.get_items()[0].get_items()[0]:
                print("Typ tisku: Tisknout všechny stránky")
            elif selected_radiobutton == self.get_items()[0].get_items()[1]:
                print("Typ tisku: Tisknout stránky v určitém rozsahu")
            print("Počet kopií: ", pocet)
            print("Tisknout oboustranně: ", is_double)

window = Window()

radio_group = RadiobuttonGroup()
form = Form(radio_group)
button = ButtonGroup(form)

group = Group().set_items([form, button])

window.set_widget(group)
window.main_loop()