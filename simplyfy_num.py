def simplify(number):
    num_str = str(number)
    ans_str = ''
    if num_str == '0':
          return ''

    # making the ans_str
    for i in range(len(num_str)):
            temp_str = "1" + '0'*(len(num_str) - (i+1)) # tells to multiply with 100, 1000 or the place value 
            if num_str[i] != '0':
                ans_str += f"{num_str[i]}*" + temp_str + "+" # skips '0' and gives adds ans to ans_str
        
    #slicing on the base of last digit 
    if num_str[len(num_str) - 1 ] == '0':
        return ans_str[0: len(ans_str)-1]
    else:
         return ans_str[0: len(ans_str)-3]

b = simplify(605)
print(b)