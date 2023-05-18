arqs = []
while True:
    arq = input()
    if arq == "0":
        break
    else:
        arqs.append(arq)
print()
for i in arqs:
    try:
        with open(i, "r") as file:
            with open("saida(9-10).txt", "a") as sai:
                for j in file:
                    lin = j.strip("\n")
                    sai.write(f"{lin}\n")
    except FileNotFoundError:
        print("Nao tem o arquivo")