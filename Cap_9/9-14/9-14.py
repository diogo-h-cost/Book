try:
    with open("test_9-14.txt", "r") as arq:
        with open("nov_9-14", "w") as file:
            for i in arq:
                for j in i:
                    linha = j.strip(" ")
                    file.write(linha.strip("\n"))
except FileNotFoundError:
    print("Arquivo inexistente")