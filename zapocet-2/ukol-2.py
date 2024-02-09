from fmw import *
from lst import *

english_wordlist = cons("cat", cons("mountain", cons("ocean", cons("book", cons("sun", empty)))))
czech_wordlist = cons("kočka", cons("hora", cons("oceán", cons("kniha", cons("slunce", empty)))))

def list_find_index(pred, lst, index=0):
    if is_empty(lst):
        return None  
    elif pred(first(lst)):
        return index
    else:
        return list_find_index(pred, rest(lst), index + 1)  

def list_nth(lst, i):
    return first(lst) if i == 0 else list_nth(rest(lst), i - 1)

def english_to_czech(string):
    def translate_word(word):
        index = list_find_index(lambda x: x == word, english_wordlist)
        return list_nth(czech_wordlist, index) if index is not None else None

    translated_words = filter(None, map(translate_word, string.split()))
    return ' '.join(translated_words) if string else None

def czech_to_english(string):
    def translate_word(word):
        index = list_find_index(lambda x: x == word, czech_wordlist)
        return list_nth(english_wordlist, index) if index is not None else None

    translated_words = filter(None, map(translate_word, string.split()))
    return ' '.join(translated_words) if string else None

def radiobutton_group(count, selected, labels=None, i=0):
    if count == i:
        return empty_widget
    else:
        radio_button = radiobutton(i == selected, i, 20 + i * 70, 5)
        label_widget = label(labels[i], 40 + i * 70, 5)
        group_widget = group(radio_button, label_widget)

        return group(group_widget, radiobutton_group(count, selected, labels, i + 1))

def radiobutton_group_update(selected, index, is_selected):
    return index if is_selected else selected

def what_the_language(lang, string):
    if lang == 0:
        return english_to_czech(string)
    else:
        return czech_to_english(string)

def content(state):
    lang, string = state
    labels = ["English", "Czech"]

    def create_entry_group():
        return group(
            entry(string, True, 20, 40),
            label(what_the_language(lang, string), 20, 70),
        )

    def create_new_entry_group():
        return group(
            entry("", True, 20, 40),
            label("", 20, 70),
        )

    new_entry_group = create_entry_group() if type(string) != bool else create_new_entry_group()
    new_radiobutton_group = radiobutton_group(2, lang, labels=labels)


    return group(
        new_entry_group,
        new_radiobutton_group
    )

def update(state, action):
    lang, selected = state
    if type(action[1]) == str:
        return (lang, action[1])
    else:
        new_lang = action[0]
        return (new_lang, radiobutton_group_update(selected, action[1], action[0]))

display_window_and_loop(content, [0, "Your text..."], update)