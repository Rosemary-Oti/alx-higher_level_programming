#!/usr/bin/python3

def uppercase(s):
    for c in s:
        if 'a' <= c <= 'z':
            offset = ord('A') - ord('a')
            print(chr(ord(c) + offset), end="")
        else:
            print(c, end="")
    print()
