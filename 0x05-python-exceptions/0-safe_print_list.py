#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    For i in range(x):
        try:
            print(""format(my_list=[]) end="")
            count += 1
        except IndexError:
            break
    return count
