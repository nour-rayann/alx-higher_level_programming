#!/usr/bin/env python3
def no_c(my_string):
    my_string = list(my_string)
    n = my_string.count('c')
    if n > 0:
        while n:
            my_string.remove('c')
            n = n - 1
    n = my_string.count('C')
    if n > 0:
        while n:
            my_string.remove('C')
            n = n - 1
    my_string = ''.join(my_string)
    return my_string
