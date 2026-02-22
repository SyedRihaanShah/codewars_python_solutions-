def count_feelings(st,arr):
    count = 0
    for word in arr:
        valid = True 
        for char in word :
            if char not in st :
                valid = False 
                break
        
        if valid == True:
            count += 1
            
    
    return f'{count} feelings'

b = count_feelings('yliausoenvjw',  ['anger', 'awe', 'joy', 'love', 'grief'])
print(b)