def soma(l):
    tot = 0
    for i in range(len(l)):
        tot += l[i]
    return tot

l = [1, 7, 2, 9, 15]
print(soma(l))
print(soma([7, 9, 12, 3, 100, 20, 4]))