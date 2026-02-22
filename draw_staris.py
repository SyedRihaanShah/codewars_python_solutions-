def draw_stairs(n):
    result = ""
    for i in range(n):
        if i == n-1:
            result += i * ' ' + "I"
        else:
             result += i * ' ' + "I" + "\n"
    return result

a = draw_stairs(100)
print(a)