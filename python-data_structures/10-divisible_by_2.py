#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    if my_list == []:
        return None
    
    new_list = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:      # ← هنا الفحص الصحيح
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
