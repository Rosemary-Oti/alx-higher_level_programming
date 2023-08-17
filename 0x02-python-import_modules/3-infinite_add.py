#!/usr/bin/python3

import sys

def main():
    args = sys.argv[1:]
    total_sum = sum(int(arg) for arg in args)
    print(total_sum)

if __name__ == "__main__":
    main()
