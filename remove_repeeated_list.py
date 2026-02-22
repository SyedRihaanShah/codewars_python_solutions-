def remove_(integer_list,value_list):
    new_list = []
    for num in integer_list:
        if num not in value_list:
            new_list.append(num)
    return new_list

b = remove_([1, 1, 2, 3, 1, 2, 3, 4], [1, 3])
print(b)