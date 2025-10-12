#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            value_1 = my_list_1[i]
            value_2 = my_list_2[i]

            if not isinstance(value_1, (int, float)) or not isinstance(value_2, (int, float)):
                    print("wrong type")
            else:
                try:
                    result = value_1 / value_2
                except ZeroDivisionError:
                    print("Division by 0")
        except IndexError:
            print("Out of range")
        finally:
            new_list.append(result)
    return new_list


if __name__ == "__main__":

    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
