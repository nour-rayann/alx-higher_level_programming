#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        i = my_list[0]
        for count in range(len(my_list)):
            if i < my_list[count]:
                i = my_list[count]
    else:
        return None
    return i
