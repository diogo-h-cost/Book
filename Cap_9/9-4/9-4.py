arq1 = input()
arq2 = input()

try:
    with open(arq1, "r") as fil1, open(arq2, "r") as fil2:
        with open("saida(9-4).txt", "w") as sai:
            sai.write(f"{fil1.read()}\n")
            sai.write(fil2.read())
except FileNotFoundError:
    print("Nao tem o arquivo")