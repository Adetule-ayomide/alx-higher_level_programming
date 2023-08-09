#!/usr/bin/python3
def uppercase(str):
    new_str = list()
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            new_str.append(chr(ord(i) - 32))
        else:
            new_str.append(i)
    print('{}'.format("".join(new_str)), end='')
    print()
