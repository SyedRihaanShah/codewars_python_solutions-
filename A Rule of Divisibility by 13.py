def thirt(n):
    sequence = [1,10,9,12,3,4]

    while True : # infinite loop to make sure we get a constant number
        total = 0
        n_str = str(n) # makes the new number strinh everytime

        for i in range(len(n_str)):
            digit = int(n_str[-(i+1)]) # takes the digits from left to right 
            total += digit * sequence[i % len(sequence)] # repeates the sequence 
        
        if total == n :
            return total
        
        n = total

a = thirt(1234567)
print(a) # test case