def digital_root(n):
    


    while True :
        sum = 0
        n_str = str(n)
        for num in  n_str:
            sum += int(num)
        
        if sum < 10:
            
            return sum 
        
        n = sum 
    

n = digital_root(942)
print(n)
