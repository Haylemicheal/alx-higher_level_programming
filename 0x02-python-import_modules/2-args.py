#!/usr/bin/python3
import sys
argv = sys.argv

print("{} arguments{}".format(len(argv) - 1, ":" if len(argv) > 1 else "."))
for i in range(1, len(argv)):
    print("{}: {}".format(i, argv[i]))
