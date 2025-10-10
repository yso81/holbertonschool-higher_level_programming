#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    sorted_dict = {key: a_dictionary[key] for key in sorted_keys}
    print(sorted_dict)


if __name__ == "__main__":

    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)
