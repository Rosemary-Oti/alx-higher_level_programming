#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0

    for item in my_list[:x]:
        try:
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                printed_count += 1
        except (ValueError, TypeError):
            continue

    print()  # Add a newline after printing
    return printed_count
