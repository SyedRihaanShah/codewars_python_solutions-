from math import gcd

def has_integer_roots(equation):
    for i in range(1, len(equation) - 1): # iterating till len - 1 bcoz we dont want to find gcd with costant 
        b = equation[0]
        b = gcd(b, equation[i]) # updates gcd cummulativelty 

    
    if equation[len(equation) - 1] % b == 0:
        return True
    else:
        return False 
    
b = has_integer_roots([6,9,15,21,134])
print(b)
    
    
    
    