#!/usr/bin/python3
import hidden_4

names_defined = dir(hidden_4)

for name in names_defined:
    if not name.startswith("__"):
        print(name)
