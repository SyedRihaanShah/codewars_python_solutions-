def sum_strings(x, y):
    num_1, num_2 = int(x), int(y)
    result = num_1 + num_2
    return str(result)

b = sum_strings('1', '2')
print(b, type(b))