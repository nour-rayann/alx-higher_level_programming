#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        c = sentence[0]
    else:
        c = "None"
    tuple = ()
    if len(sentence):
        tuple = len(sentence), c
    else:
        tuple = 0, c
    return tuple
