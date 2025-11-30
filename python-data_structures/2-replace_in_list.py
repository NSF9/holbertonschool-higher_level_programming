#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    
    NewValue = element
    if idx < 0:
        return None
    else:
        my_list[idx] = NewValue
        return my_list 
