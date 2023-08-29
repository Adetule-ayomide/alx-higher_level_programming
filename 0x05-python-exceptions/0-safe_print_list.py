#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        if count < x:
            try:
                print(i, end=" ")
                    count += 1
        else:
            break
            except IndexError:
                pass
    print()
    return count
