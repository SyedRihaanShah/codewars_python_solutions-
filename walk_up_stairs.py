def stairs(n):
    str_t = ''
    intial_num = 6 * n
    if n > 1 :
        intial_num = 6 * n - 10
    for i in range(1 , n+1):
        #spaces
        if i != 1:
            intial_num -= 4
        str_t += ' ' * (intial_num)
        #increment part
        for j in range(1, i + 1):
            str_t += str(j) + ' '
        #decrement part
        for j in range(i, 0, -1):
            str_t += str(j) + ' '
        
        str_t += '\n'
    
    return str_t
                   


b = stairs(6)
print(b)