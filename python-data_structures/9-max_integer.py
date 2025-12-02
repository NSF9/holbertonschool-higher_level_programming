#!/usr/bin/python3
def max_integer(my_list=[]):

    if my_list == []:
        return None

    Max_value = my_list[0]

    for i in my_list:
        if i > Max_value:
            Max_value = i

    return Max_value
