def parts_sums(ls):
    parts_ls = []
    for i in range(len(ls)):
        for j in range(i - len(ls)):
            sum = 0
            sum += ls[j]
            parts_ls.append(sum)

    return parts_ls


b =parts_sums([0, 1, 3, 6, 10])
print(b)