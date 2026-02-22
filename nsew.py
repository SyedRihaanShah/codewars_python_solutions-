def is_valid_walk(walk):
    n_sum = walk.count('n')
    s_sum = walk.count('s')
    e_sum = walk.count('e')
    w_sum = walk.count('w')

    if n_sum == s_sum and e_sum == w_sum and n_sum + s_sum + e_sum + w_sum == 10:
        return True
    else:
        return False
    
b = is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])
print(b)