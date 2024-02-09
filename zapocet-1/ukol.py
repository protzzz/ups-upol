from omw import *

class FullnameEntryGroup(Group):
    def __init__(self):
        super().__init__()
        label1 = Label().set_text("Name:").move(5, 5)
        entry1 = Entry().move(110, 0)
        entry1.set_text("Your name...")
        label2 = Label().set_text("Surname:").move(5, 33)
        entry2 = Entry().move(110, 30)
        entry2.set_text("Your surname...")
        self.set_items([label1, label2, entry1, entry2])

    def get_name(self):
        return self.get_items()[2]

    def get_surname(self):
        return self.get_items()[3]

class RadiobuttonGroup(Group):
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

class EmailAndPasswordGroup(Group):
    def __init__(self):
        super().__init__()
        label1 = Label().set_text("E-mail:").move(5, 93)
        label2 = Label().set_text("Password:").move(5, 148)
        entry1 = Entry().move(110, 90)
        entry2 = Entry().move(110, 145)
        label3 = Label().move(110, 120).set_text("Write your e-mail to verify!")
        label4 = Label().move(5, 120).set_text("Verify process:")
        label5 = Label().move(110, 180).set_text("Write your password to verify!")
        label6 = Label().move(5, 180).set_text("Verify process:")
        self.set_items([label1, label2, entry1, entry2, label3, label4, label5, label6])

    def get_email(self):
        return self.get_items()[2]

    def get_password(self):
        return self.get_items()[3]

    def get_validate_email(self):
        return self.get_items()[4]

    def get_validate_password(self):
        return self.get_items()[6]

    def validate_email(self):
        text = self.get_email().get_text()
        if "@" not in text:
            text = "Your e-mail address doesn't have '@' sign!"
        else:
            parts = text.split(".")
            if len(parts) < 2 or len(parts[-1]) < 2:
                text = "E-mail isn't valid (e.g., .com, .cz, .ua, etc.)"
            else:
                text = "The e-mail is verified!"
        self.get_validate_email().set_text(text)
        return self

    def validate_password(self):
        text = self.get_password().get_text()
        password_strength = 0
        description = ""

        if len(text) >= 8:
            password_strength += 1
            description += "Minimum 8 characters. "
        if any(c.isupper() for c in text):
            password_strength += 1
            description += "At least one uppercase letter. "
        if any(c.islower() for c in text):
            password_strength += 1
            description += "At least one lowercase letter. "
        if any(c.isdigit() for c in text):
            password_strength += 1
            description += "At least one digit. "
        if any(not c.isalnum() for c in text):
            password_strength += 1
            description += "At least one special character. "

        if password_strength == 0:
            description = "Very Weak"
        elif password_strength == 1:
            description = "Weak"
        elif password_strength == 2:
            description = "Moderate"
        elif password_strength == 3:
            description = "Strong"
        elif password_strength >= 4:
            description = "Very Strong"
            
        self.get_validate_password().set_text(description)
        return self

    def ev_change(self, sender):
        super().ev_change(sender)
        if sender == self.get_email():
            self.validate_email()
        elif sender == self.get_password():
            self.validate_password()
            
class ButtonGroup(Group):
    def __init__(self, form):
        super().__init__()
        self.form = form
        button = Button().move(60, 220).set_text("Show personal information")
        self.set_items([button])

    def display_text(self):
        name = self.form.get_name().get_text()
        surname = self.form.get_surname().get_text()
        sex_widget = self.form.get_radiobutton_group().get_selected()
        labels = self.form.get_label().get_items()
        
        if sex_widget:
            index = self.form.get_radiobutton_group().get_items().index(sex_widget)
            sex = labels[index+1].get_text()
        else:
            sex = "Not selected"

        email = self.form.get_email().get_text()
        password = self.form.get_password().get_text()
        
        print("Name:", name)
        print("Surname:", surname)
        print("Sex:", sex)
        print("E-mail:", email)
        print("Password:", password, "\n")

    def ev_button_clicked(self, sender, button):
        super().ev_button_clicked(sender, button)
        self.display_text()

class Form(Group):
    def __init__(self, fullname_group, email_and_password_group):
        super().__init__()
        self.fullname_group = fullname_group
        self.email_and_password_group = email_and_password_group
        radio1 = Radiobutton().move(110, 65)
        radio2 = Radiobutton().move(200, 65)
        radiobutton_group = RadiobuttonGroup().set_items([radio1, radio2])
        label1 = Label().set_text("Sex:").move(5, 65)
        label2 = Label().set_text("Male").move(130, 65)
        label3 = Label().set_text("Female").move(220, 65)
        label_group = Group().set_items([label1, label2, label3])
        self.set_items([radiobutton_group, label_group, fullname_group, email_and_password_group])

    def get_radiobutton(self):
        return self.get_items()[0].get_selected()

    def get_label(self):
        return self.get_items()[1]

    def get_name(self):
        return self.fullname_group.get_name()

    def get_surname(self):
        return self.fullname_group.get_surname()

    def get_email(self):
        return self.email_and_password_group.get_email()

    def get_password(self):
        return self.email_and_password_group.get_password()
    
    def get_email_and_password_group(self):
        return self.email_and_password_group()

    def get_radiobutton_group(self):
        return self.get_items()[0]

    def set_fields(self, fields):
        radiobuttons = self.get_radiobutton()
        labels = self.get_label()
        name = self.get_name()
        surname = self.get_surname()
        email_and_password_group = get_email_and_password_group()
        self.set_items([radio_buttons, labels, name, surname, email_and_password_group] + fields)
        return self

    def get_fields(self):
        return self.get_items()[3:]


window = Window()
fullname = FullnameEntryGroup()
email_and_password = EmailAndPasswordGroup()

form = Form(fullname, email_and_password)
button = ButtonGroup(form)

group = Group().set_items([form, button])

window.set_widget(group)
window.main_loop()
