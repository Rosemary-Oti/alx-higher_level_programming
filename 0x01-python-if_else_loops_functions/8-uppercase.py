#!/usr/bin/python3

def uppercase(s):
    offset = ord('A') - ord('a')
    for c in s:
        if 'a' <= c <= 'z':
            print(chr(ord(c) + offset), end="")
        else:
            print(c, end="")
    print()
