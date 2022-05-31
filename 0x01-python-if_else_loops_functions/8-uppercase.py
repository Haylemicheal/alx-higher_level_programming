#!/usr/bin/python3
def uppercase(str):
    for c in str:
        i = ord(c)
        if (i >= 97 and i < 123):
            i = i - 32
            c = chr(i)
        print("{}".format(c), end="")
    print("{}".format(""))
