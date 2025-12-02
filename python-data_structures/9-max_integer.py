#!/usr/bin/python3
def max_integer(my_list=[]):
    Max_value = my_list[0]
    if my_list == 0:
        return None
    
    for i in my_list:
        if i > Max_value: 
            Max_value = i

    return Max_value
