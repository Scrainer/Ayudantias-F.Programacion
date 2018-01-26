a = "mensaje"
c = "abcdefg"
i = len(c) - 1
for b in a:
    print(b * c.index(c[i]))
    i -= 1

L = [5, 3, 8, 2, 7]
A = [0] * 10
indice = 3
for valor in L:
    if valor < 6:
        indice -= 1
    else:
        indice += 1
    A[indice] = valor
print(set(A))
