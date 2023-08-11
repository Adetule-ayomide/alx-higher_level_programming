#!/usr/bin/python3.8

import hidden_4


def main():
    brk = list()
    j = ""
    for i in dir(hidden_4):
        j = i
        brk.append(j)
        if j[0] != "_":
            print("{}".format(j), end="\n")

if __name__ == "__main__":
    main()
