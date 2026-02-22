from math import gcd


def solution(lst):
    g = lst[0]
    t_l = []
    for num in lst[1: ] :
        g = gcd(g, num)
        t_l.append(g)



    return t_l


b = solution([6,9,12])
print(b)