arqs = []
while True:
    arq = input()
    if arq == "0":
        break
    else:
        arqs.append(arq)
        print(arqs)
print()
for i in arqs:
    try:
        with open(i, "r") as file:
            for j in file:
                lin = j.strip("\n")
                print(lin)
            print()
    except FileNotFoundError:
        print("Nao tem o arquivo")