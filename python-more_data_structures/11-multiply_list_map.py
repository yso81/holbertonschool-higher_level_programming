#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    result = list(map(lambda x: x * number, my_list))
    return result


if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 6]
    new_list = multiply_list_map(my_list, 4)
    print(new_list)
    print(my_list)
