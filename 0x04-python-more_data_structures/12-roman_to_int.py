#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0
    total = 0
    
    for ch in reversed(roman_string):
        value = rom_n.get(ch, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total
