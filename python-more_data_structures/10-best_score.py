#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        s_dict = sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)

        for key, value in s_dict:
            return key
            break
