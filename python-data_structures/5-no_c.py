#!/usr/bin/python3
def no_c(my_string):
    sentence_without_c = ""

    for ch in my_string:
        if ch != "c" and ch != "C":
            sentence_without_c += ch

    return sentence_without_c
