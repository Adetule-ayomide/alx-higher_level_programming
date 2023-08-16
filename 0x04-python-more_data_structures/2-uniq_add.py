#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list = set(my_list)
    add_list = 0
    for i in new_list:
        add_list += i
    return add_list
