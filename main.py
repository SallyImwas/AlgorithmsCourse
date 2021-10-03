"""
This is a python program that measure how much two texts are relevant
"""


def del_stop_words(text):
    irr_words = ["a ", "an ", "the ", "is "]
    text.lower()
    for irr_word in irr_words:
        if irr_word in text:
            text = text.replace(irr_word, "")
    return text


def get_top_six(text):
    sixth_common = {}
    for word in text:
        if word not in sixth_common:
            if len(sixth_common) < 6:
                sixth_common[word] = 1
            else:
                pass
        else:
            sixth_common[word] = sixth_common[word] + 1


def is_relevant(text1_list, text2_list):
    pass


first_text = input("Enter the first text,please\n")
second_text = input("Enter the second text,please\n")
first_text = del_stop_words(first_text)
second_text = del_stop_words(second_text)

print(first_text, second_text, end="\n")
