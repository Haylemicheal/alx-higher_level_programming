#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1

if (number < 0):
    sign = -1
    number = number * sign

mod = number % 10

if (mod == 0):
    print(f"Last digit of {number} is {mod} and is 0")
elif (mod < 6 or sign == -1):
    print(f"Last digit of {number*-1} is {mod*-1} "
          f"and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {mod} and is greater than 5")
