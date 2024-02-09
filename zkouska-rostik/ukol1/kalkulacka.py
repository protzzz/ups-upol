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
            text = "Invalid format"
        self.get_validation_label().set_text(text)
        return self

    def ev_change(self, sender):
        super().ev_change(sender)
        if sender == self.get_entry():
            self.validate()
    
class Form(Group):
    def __init__(self):
        super().__init__()
        radiobutton_x = 60
        radiobuttons = []
        for i in range(4):
            radiobuttons.append(Radiobutton().move(radiobutton_x, 105))
            radiobutton_x += 40
        button = Button()
        l1 = Label().move(63,130).set_text("+")
        l2 = Label().move(103,130).set_text("-")
        l3 = Label().move(143,130).set_text("*")
        l4 = Label().move(183,130).set_text("/")
        l5 = Label().move(90,75)
        labels = Group().set_items([l1,l2,l3,l4,l5])
        radiobuttons = RadiobuttonGroup().set_items(radiobuttons)
        self.set_items([button,radiobuttons,labels])

    def get_send_button(self):
        return self.get_items()[0]

    def get_radio_button(self):
        return self.get_items()[1]

    def get_radio_label(self):
        return self.get_items()[2]
    
    def set_fields(self, fields):
        if all(isinstance(field, IntegerEntryField) for field in fields):
            button = self.get_send_button()
            radio_buttons = self.get_radio_button()
            radio_labels = self.get_radio_label()
            self.set_items([button,radio_buttons, radio_labels] + fields)
        else:
            raise ValueError("items should be the instances of IntegerEntryField")
        return self

    def get_fields(self):
        return self.get_items()[3:]

    def get_selected_operation(self):
        selected_radio = self.get_radio_button().get_selected()
        index = 0
        if selected_radio:
            radio_items = self.get_radio_button().get_items()
            for radio in radio_items:
                if radio.is_selected():
                    return self.get_radio_label().get_items()[index].get_text()
                else:
                    index += 1
        return None

    def calculate(self, num1, num2, operation):
        counter = 0
        if operation == "+":
            counter = num1 + num2
        elif operation == "-":
            counter = num1 - num2
        elif operation == "*":
            counter = num1 * num2
        elif operation == "/":
            counter = num1 / num2
        return counter

    def ev_button_clicked(self, sender, button):
        super().ev_button_clicked(sender, button)
        operation = self.get_selected_operation()
        num1 = self.get_fields()[0].get_entry().get_value()
        num2 = self.get_fields()[1].get_entry().get_value()
        if operation:
            result = self.calculate(num1, num2, operation)
            self.get_radio_label().get_items()[-1].set_text("Result:  " + str(result))
        print(result)

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

    
              
e1 = IntegerEntryField().move(10,0)
e1.get_label().set_text("Cislo 1:")
e2 = IntegerEntryField().move(160,0)
e2.get_label().set_text("Cislo 2:")


f = Form().set_fields([e1, e2])
f.get_send_button().move(100, 160).set_text("Odešli")

w = Window().set_widget(f)
w.main_loop()