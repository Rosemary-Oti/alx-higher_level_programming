#!/usr/bin/python3
import sys

num_args = len(sys.argv) - 1

if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
else:
    print(f"{num_args} arguments:")
    for i in range(num_args):
        print(f"{i + 1}: {sys.argv[i + 1]}")
