arquivo = open("teste(9-2).txt", "w")

ini = int(input())
fim = int(input())

for linha in range(ini, fim+1):
    arquivo.write(f"{linha}\n")
    
arquivo.close()