def grabscrab(said, possible_words):
    final_list = []
    for i in range (len(possible_words)):
        if sorted(said) == sorted(possible_words[i]):
            value = possible_words[i]
            final_list.append(value)

    return final_list


b = grabscrab("ortsp", ["sport", "parrot", "ports", "matey"])
print(b)
