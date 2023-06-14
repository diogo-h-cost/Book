with open("9-5.txt", "w") as inv:
    with open("pares(9-3).txt") as par:
        cont = par.readlines()
        for n in cont[::-1]:
            inv.write(n)