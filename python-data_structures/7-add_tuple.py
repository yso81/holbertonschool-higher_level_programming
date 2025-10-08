#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    max_len = max(len_a, len_b)

    result_list = []
    for i in range(max_len):
        val_a = 0
        val_b = 0

        if i < len_a:
            val_a = tuple_a[i]

        if i < len_b:
            val_b = tuple_b[i]
        
        result_list.append(val_a + val_b)
    
    return tuple(result_list)
    #result = []
    #for i in range(len(tuple_a)):
        #result.append(tuple_a[i] + tuple_b[i])
    
    #result = tuple(tuple_a[i] + tuple_b[i] for i in range(len(tuple_a)))
    #return result
if __name__ == "__main__"
    #tuple_a = (1, 89)
    #tuple_b = (88, 11)
    #new_tuple = add_tuple(tuple_a, tuple_b)
    #print(new_tuple)

    #print(add_tuple(tuple_a, (1, )))
    #print(add_tuple(tuple_a, ()))
