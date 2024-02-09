from omw import *
class IntegerEntry(Entry):
    def get_value(self):
        return int(self.get_text())

    def set_value(self, value):
        return self.set_text(str(value))
    
    def is_valid(self):
        return self.get_text().isdecimal()

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
            text = "Není číslo"
        self.get_validation_label().set_text(text)
        return self


class Form(Group):
    def __init__(self):
        super().__init__()
        button = Button()
        self.set_items([button])

    def get_send_button(self):
        return self.get_items()[0]

    def set_fields(self, fields):
        # přidat kontrolu zda fields jsou položky formuláře
        button = self.get_send_button()
        self.set_items([button] + fields)
        return self

    def get_fields(self):
        return self.get_items()[1:]

    def ev_button_clicked(self, sender, button):
        super().ev_button_clicked(sender, button)
        for field in self.get_fields():
            field.validate()
              
e1 = IntegerEntryField()
e1.get_label().set_text("Věk:")
e2 = IntegerEntryField().move(0, 80)
e2.get_label().set_text("Oblíbené číslo:")
f = Form().set_fields([e1, e2])
f.get_send_button().move(0, 160).set_text("Odešli")
w = Window().set_widget(f)
w.main_loop()