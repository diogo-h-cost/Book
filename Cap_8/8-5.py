def pesquise(L, valor):
    for x in L:
        if x == valor:
            return True
    return None

L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))