#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        x = ""
        if i % 3 != 0 and i % 5 != 0:
            print("{}".format(i), end=" ")
            continue
        if i % 3 == 0:
            x = x + "Fizz"
        if i % 5 == 0:
            x = x + "Buzz"
        print("{}".format(x), end=" ")
