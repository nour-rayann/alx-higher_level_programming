#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    n = new_string.count('c')
    if n > 0:
        while n:
            new_string.remove('c')
            n = n - 1
    n = new_string.count('C')
    if n > 0:
        while n:
            new_string.remove('C')
            n = n - 1
    new_string = ''.join(new_string)
    return new_string
