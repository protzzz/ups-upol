# Prototypy základních ovládacích prvků.
# Prvky lze posouvat zprávou move.

from proto import obj

# Prototyp widget
# Prototyp všech ovládacích prvků.
widget = obj.clone()
widget.set_name("widget")

# Prototyp label
# Má vlastnosti x, y a text.
label = widget.clone()
label.set_name("label")
label.add_slot("x")
label.add_slot("y")
label.set_x(0)
label.set_y(0)

label.add_slot("text")
label.set_text("")

def label_move(call_super, self, dx, dy):
    self.set_x(self.x() + dx)
    self.set_y(self.y() + dy)
    return self
    
label.set_slot("move", label_move)


# Prototyp group skupin prvků.
# Má vlastnost items.
group = widget.clone()
group.set_name("group")
group.add_slot("items")
group.set_items([])


def group_clone(call_super, self):
    clone = call_super()
    cloned_items = []
    # Klonování skupiny způsobí
    # klonování jejích prvků:
    for item in self.items():
        cloned_items += [item.clone()]
    clone.set_items(cloned_items)
    return clone

group.set_slot("clone", group_clone)


def group_move(call_super, self, dx, dy):
    for item in self.items():
        item.move(dx, dy)
    return self

group.set_slot("move", group_move)

"""
>>> label1 = label.clone()
>>> label1.move(20, 30)
<label at 4351586256>
>>> print(label1.x(), label1.y())
20 30
>>> label2 = label.clone()
>>> group1 = group.clone().set_items([label1, label2])
>>> group1.move(10, 0)
>>> print(label1.x(), label1.y())
30 30
>>> print(label2.x(), label2.y())
10 0
>>> group2 = group1.clone()
>>> group2.move(0, 10)
<group at 4352868240>
>>> for item in group2.items():
        print(item.x(), item.y())

30 40
10 10
>>> for item in group1.items():
        print(item.x(), item.y())

    
30 30
10 0
"""


