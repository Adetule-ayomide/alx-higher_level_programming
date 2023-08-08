#!/usr/bin/python3
#for i in range(0, 10):
    #for j in range(i + 1, 10):
        #if(i == 8 and j == 9):
            #print("{}{}".format(i, j))
        #else:
            #print("{}{}".format(i, j), end=", ")

for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
