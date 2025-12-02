#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list

    for i in my_list:
     if my_list[i - 1] == idx:
        break
    del my_list[idx]

    return my_list
