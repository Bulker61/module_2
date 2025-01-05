def pass_(n):
    resuit = ""
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                resuit += str(i) + str(j)
    return resuit

print('Введите число: ')
print(pass_(int(input())))