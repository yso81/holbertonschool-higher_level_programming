#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    if len(my_list) == 1:
        return my_list

    # for current_index in range(len(my_list)):
    #     if current_index == idx:
    #         my_list[idx] = element

    my_list[idx] = element

    return my_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_element = 9
    idx = 1
    new_list = replace_in_list([6, 7, 8, 9, 10], 1, 8)

#print(new_list)
#print(my_list)