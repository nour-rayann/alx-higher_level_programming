#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = str[i]
        if ord(c) > 96 and ord(c) < 123:
            c = chr(ord(c) - 32)
        if i < (len(str) - 1):
            print("{}".format(c), end="")
        else:
            print(c)
