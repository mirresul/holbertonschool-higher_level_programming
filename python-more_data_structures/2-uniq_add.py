#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []

    for element in my_list:
        if element not in unique:
            unique.append(element)

    total = 0
    for num in unique:
        total += num

    return total
