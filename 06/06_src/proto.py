# Jednoduchá knihovna na ukázku prototypového objektového programování.
#
# Pro použití stačí importovat objekt obj:
#
# from proto import obj
import typing

class LookupError(TypeError):
    pass

def get_slots(obj):
    return object.__getattribute__(obj, "slots")

def set_slots(obj, slots):
    object.__setattr__(obj, "slots", slots)

def set_slot(obj, slot, value):
    slots = get_slots(obj)
    slots[slot] = value
    return obj

def lookup(obj, message):
    slots = get_slots(obj)
    if message in slots.keys():
            return obj, slots[message]
    if "parent" in slots.keys():
        return lookup(slots["parent"], message)
    raise LookupError

def eval_handler(owner, handler, receiver, message, *args):
    if isinstance(handler, typing.Callable):
        def call_super():
            return send(receiver, owner.parent(), message, *args)
        return handler(call_super, receiver, *args)
    else:
        return handler    
    
def send(receiver, obj, message, *args):
    try:
        owner, handler = lookup(obj, message)
    except LookupError:
        raise TypeError(f"Object {obj} does not understand {message}.")
    return eval_handler(owner, handler, receiver, message, *args)
    
class Object:
    def __init__(self):
        set_slots(self, {})

    def __getattr__(self, slot):
        return lambda *args: send(self, self, slot, *args)

    def __repr__(self):
        try:
            name = self.name()
        except:
            name = "object"
        return f"<{name} at {id(self)}>"

# Základní objekt
obj = Object()

def object_set_slot(call_super, self, slot, value):
    slots = get_slots(self)
    slots[slot] = value
    return self

set_slot(obj, "set_slot", object_set_slot)

def object_clone(call_super, self):
    return set_slot(Object(), "parent", self)

obj.set_slot("clone", object_clone)

def object_add_slot(call_super, self, name):
    self.set_slot(name, None)
    def set_value(call_super, self, val):
        return self.set_slot(name, val)
    self.set_slot("set_" + name, set_value)
    return self

obj.set_slot("add_slot", object_add_slot)

def object_print(call_super, self):
    slots = get_slots(self)
    header = f"Object {self} slots"
    print(header)
    print("-" * len(header))
    for key in slots.keys():
        print(f"{key}:\t{repr(slots[key])}")
    print()
    return self

obj.set_slot("print", object_print)

def object_understand(call_super, self, message):
    try:
        lookup(self, message)
        return True
    except LookupError:
        return False

obj.set_slot("understand", object_understand)

def object_send(call_super, self, message, *args):
    return send(self, self, message, *args)

obj.set_slot("send", object_send)

obj.add_slot("name")
obj.set_name("object")


