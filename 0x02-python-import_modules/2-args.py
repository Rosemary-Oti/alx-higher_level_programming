#!/usr/bin/python3
import sys

num_args = len(sys.argv) - 1
args_list = sys.argv[1:]

print(f"Number of argument(s): {num_args}")
if num_args == 0:
    print("0 arguments.")
else:
    print("1 argument:")
    for i in range(num_args):
        print(f"{i + 1}: {sys.argv[i + 1]}")
