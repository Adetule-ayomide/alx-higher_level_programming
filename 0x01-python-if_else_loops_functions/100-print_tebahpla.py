#!/usr/bin/python3
for letter in range(26):
    if(letter % 2 == 0):
        print(chr(122 - letter), end="")
    else:
        print(chr(90 - letter),end="")
