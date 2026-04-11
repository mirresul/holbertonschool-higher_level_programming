#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    best_key = None
    max_value = 0

    for key in a_dictionary:
        if a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
            best_key = key

    return best_key
