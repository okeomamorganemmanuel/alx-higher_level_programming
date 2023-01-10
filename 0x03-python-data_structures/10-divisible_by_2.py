#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if isinstance(my_list, list):
        div_list = my_list.copy()

        for i in range(len(my_list)):
            if div_list[i] % 2 == 0:
                div_list[i] = True
            else:
                div_list[i] = False
        return div_list
