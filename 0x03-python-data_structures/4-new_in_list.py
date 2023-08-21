#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if idx < 0:
        return list
    elif idx >= len(my_list):
        return list
    else:
        my_list[idx] = element
        return my_list
