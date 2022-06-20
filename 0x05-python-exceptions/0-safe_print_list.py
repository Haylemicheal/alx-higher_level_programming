#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        c = 0
        try:
            print(my_list[i], end="")
            c = c + 1
        except Exception:
            break
    print('')
    return c
