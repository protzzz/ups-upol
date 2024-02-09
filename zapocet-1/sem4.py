from omw import *

class IntegerEntry(Entry):
    def get_value(self):
        return int(self.get_text())

    def set_value(self, value):
        return self.set_text(str(value))
    
    def is_valid(self):
        return self.get_text()[1:].isdecimal() and "+" in self.get_text()


class IntegerEntryField(Group):
    def __init__(self):
        super().__init__()
        label = Label()
        entry = IntegerEntry().move(0, 20)
        validation_label = Label().move(0, 50)
        self.set_items([label, entry, validation_label])

    def get_label(self):
        return self.get_items()[0]

    def get_entry(self):
        return self.get_items()[1]

    def get_validation_label(self):
        return self.get_items()[2]

    def validate(self):
        if self.get_entry().is_valid():
            text = ""
        else:
            text = "neni telefoni cislo"
        self.get_validation_label().set_text(text)
        return self

    def ev_change(self, sender):
        super().ev_change(sender)
        if sender == self.get_entry():
            self.validate()

class EmailEntry(Entry):
     def is_valid(self):
        return "@" in self.get_text()
    
class EmailEntryField(IntegerEntryField):
    def __init__(self):
        super().__init__()
        label = Label()
        email_entry = EmailEntry().move(0, 20)
        validation_label = Label().move(0, 50)
        self.set_items([label, email_entry, validation_label])

    def validate(self):
        if self.get_entry().is_valid():
            text = ""
        else:
            text = "neni email"
        self.get_validation_label().set_text(text)
        return self

class Form(Group):
    def __init__(self):
        super().__init__()
        button = Button()
        radio1 = Radiobutton().move(35,80)
        radio2 = Radiobutton().move(75,80)
        l1 = Label().move(30,100).set_text("Muz")
        l2 = Label().move(70,100).set_text("Zena")
        lg = Group().set_items([l1,l2])
        group = RadiobuttonGroup().set_items([radio1, radio2])
        self.set_items([button,group,lg])

    def get_send_button(self):
        return self.get_items()[0]

    def get_radio_button(self):
        return self.get_items()[1]

    def get_radio_label(self):
        return self.get_items()[2]
    
    def set_fields(self, fields):
        button = self.get_send_button()
        radio_buttons = self.get_radio_button()
        radio_labels = self.get_radio_label()
        self.set_items([button,radio_buttons, radio_labels] + fields)
        return self

    def get_fields(self):
        return self.get_items()[3:]

    def ev_button_clicked(self, sender, button):
        super().ev_button_clicked(sender, button)
        for field in self.get_fields():
            if field.get_entry().is_valid():
                print(field.get_label().get_text()+ " " + field.get_entry().get_text())
        counter = 0
        for item in self.get_radio_button().get_items():
            if item.is_selected():
                print("Sex: " + self.get_radio_label().get_items()[counter].get_text())
            counter += 1
                    

class RadiobuttonGroup(Group):
    def check_item(self, item):
        if not isinstance(item, Radiobutton):
            raise TypeError("items of a radiobutton group have to be radiobuttons")
        return self

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

    
              
e1 = EmailEntryField().move(10,0)
e1.get_label().set_text("Email:")
e2 = IntegerEntryField().move(160,0)
e2.get_label().set_text("Telefoni cislo:")


f = Form().set_fields([e1, e2])
f.get_send_button().move(100, 130).set_text("Odešli")

w = Window().set_widget(f)



