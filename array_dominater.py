def dominator(arr):
    arr_dict = {}
    
    for num in arr:
        arr_dict[num] = arr_dict.get(num, 0) + 1

    if not arr_dict:
        return -1

    max_key = max(arr_dict, key=arr_dict.get)

    if arr_dict[max_key] > len(arr) // 2:
        return max_key
    else:
        return -1