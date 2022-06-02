#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    size = len(argv)
    print("{} arguments{}".format(size - 1, ":" if size > 1 else "."))
    for i in range(1, size):
        print("{}: {}".format(i, argv[i]))
