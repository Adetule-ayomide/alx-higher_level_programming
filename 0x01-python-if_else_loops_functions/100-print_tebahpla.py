#!/usr/bin/python3
for letter in range(26):
    print("{}".format(chr(122 - letter) if letter % 2 == 0 else chr(90 - letter)), end="")
