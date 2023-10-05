#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        items_sorted = sorted(a_dictionary.items())
        items_sorted.reverse()
        inverse_dict = dict(items_sorted)
        for key, value in inverse_dict.items():
            return key
            break
