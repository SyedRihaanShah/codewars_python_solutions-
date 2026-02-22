def compute_sum(n):
    sum = 0
    for i in range(1, n+1):
        temp = str(i)
        for digit in temp:
            sum += int(digit)
    return sum 

