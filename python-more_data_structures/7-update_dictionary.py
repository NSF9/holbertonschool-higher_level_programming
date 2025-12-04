#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not key in a_dictionary[key]:
        a_dictionary["city"] = value
    return a_dictionary
