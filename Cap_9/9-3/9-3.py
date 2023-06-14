with open("pareseimpares(9-3).txt", "w") as junto:
    with open("impares(9-3).txt") as imp, open("pares(9-3).txt") as par:
        for n in range(0, 1000):
            junto.write(par.readline())
            junto.write(imp.readline())