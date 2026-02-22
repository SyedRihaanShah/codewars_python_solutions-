def delete_nth(order,max_e):
    freq = {}
    l = []
    for num in order :
        if num not in l :
            l.append(num)
            freq[num] = 1
        elif num in l :
            if freq[num] == max_e:
                pass
            elif freq[num] < max_e:
                l.append(num)
                freq[num] += 1 
        
    return l

a = delete_nth([1,2,3,1,1], 2)
print(a)