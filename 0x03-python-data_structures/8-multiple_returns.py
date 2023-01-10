#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first = ""
    if len(sentence) == 0:
        length = 0
        first = None
    else:
        length = len(sentence)
        first = sentence[0]
    return tuple([length, first])
