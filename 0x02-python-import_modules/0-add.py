#!/usr/bin/python3
a = 1
b = 2
module_name = 'add_0'
module = __import__(module_name)
result = module.add(a, b)
print(f"{a} + {b} = {result}")
