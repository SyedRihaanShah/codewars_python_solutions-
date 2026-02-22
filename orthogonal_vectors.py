def is_orthogonal(u, v): 
    sum = 0

    for i in range(0, len(u) ):
        sum += u[i] * v[i]
    if sum == 0:
        return True
    else:
        return False