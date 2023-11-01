#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 101):
        copy = i
        if copy % 3 == 0 and copy % 5 == 0:
            print("FizzBuzz", end=" ")
        elif copy % 3 == 0:
            print("Fizz", end=" ")
        elif copy % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
