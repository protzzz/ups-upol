# Začátek řešení prvního úkolu ze souboru 10_movies.pty
def make_person(person_id, name, born):
    return ["person", person_id, name, born]

def get_person_id(person):
    return person[1]

def get_person_name(person):
    return person[2]

def get_person_born(person):
    return person[3]

persons = [make_person(1, "A", 1),
           make_person(2, "B", 1),
           make_person(3, "C", 2),
           make_person(4, "D", 1)]

def get_persons_born_in(persons, year):
    return filter(lambda person: get_person_born(person) == year,
                  persons)

"""
>>> list(get_persons_born_in(persons, 1))
[['person', 1, 'A', 1], ['person', 2, 'B', 1], ['person', 4, 'D', 1]]
"""

def get_persons_names(persons):
    return map(get_person_name, persons)

"""
>>> list(get_persons_names(persons))
['A', 'B', 'C', 'D']
"""
