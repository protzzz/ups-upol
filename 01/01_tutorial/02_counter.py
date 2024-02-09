# Počítadlo jako datová struktura

# counter = ["counter", value]

def make_counter():
    return ["counter", 0]

def get_counter_value(counter):
    return counter[1]

def set_counter_value(counter, value):
    counter[1] = value

# Používají abstraktní datovou strukturu counter:

def inc_counter(counter):
    set_counter_value(counter,
                      get_counter_value(counter) + 1)


def dec_counter(counter):
    set_counter_value(counter,
                      get_counter_value(counter) - 1)


c = make_counter()
