#!/usr/bin/python3
import sys

argc = len(sys.argv) - 1
if argc == 0:
    print("0 arguments.")
elif argc == 1:
    print("1 argument:")
    for i in range(1,):
        print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(argc))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
