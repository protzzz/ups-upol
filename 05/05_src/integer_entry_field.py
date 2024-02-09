from omw import *

class IntegerEntryField(Group):
    def __init__(self):
        super().__init__()
        label = Label()
        entry = Entry().move(0, 20)
        validation_label = Label().move(0, 50)
        self.set_items([label, entry, validation_label])

    def get_label(self):
        return self.get_items()[0]

    def get_entry(self):
        return self.get_items()[1]

    def validation_label(self):
        return self.get_items()[2]

    def validate(self):
        if self.get_entry().is_valid():
            text = ""
        else:
            text = "Není číslo"
        self.get_validation_label().set_text(text)
        return self

    def ev_change(self, sender):
        super().ev_change(sender)
        if sender == self.get_entry():
            self.validate()

class Form(Group):
    def __init__(self):
        super().__init__()
        button = Button()
        self.set_items(button)

    def get_fields(self):
        return self.get_items()[1:]

e1 = IntegerEntryField()
e1.get_label().set_text("Vek:")
e2 = IntegerEntryField().move(0, 60)
e2.get_label().set_text("Oblibene cislo:")
f = Form().set_fields([e1, e2])
f.set_fields([e])
w = Window().set_widget(f)
w.main_loop()