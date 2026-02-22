def duplicate_count(text):
    lower_text = text.lower()
    list_dict = {}
    count = 0
    
    for char in lower_text:
        if char not in list_dict :
            list_dict[char] = 1
        else :
            list_dict[char] += 1 
    
    for item in list_dict.values():
        if item > 1:
            count += 1

    return count


b = duplicate_count("y9qrvWm1zfod9N")
print(b)