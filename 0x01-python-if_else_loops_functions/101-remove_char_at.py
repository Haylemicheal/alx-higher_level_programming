#!/usr/bin/python3
def remove_char_at(str, n):
    val = ""
    for j, i in enumerate(str):
        if (j != n):
            val = val + i
    return val
