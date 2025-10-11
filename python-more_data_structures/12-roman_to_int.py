#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    sum = 0
    for i in range(len(roman_string)):
        if roman_string is None or not roman_string:
            return None
        else:
            current_value = roman_map[roman_string[i]]
            if i + 1 < len(roman_string) and current_value < roman_map[roman_string[i+1]]:
                sum -= current_value
            else:
                sum += current_value
    return sum


if __name__ == "__main__":

    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
