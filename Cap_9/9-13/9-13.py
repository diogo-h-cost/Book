arq = input("Arquivo: ")
ini = int(input("Linha INI: "))
fim = int(input("Linha FIM: "))

try:
    with open("test_9-13.txt", "r") as arqui:
        file = arqui.readlines()
        for i in range(ini, fim+1):
            print(file[i].strip("\n"))
except FileNotFoundError:
    print("Arquivo inexistente")