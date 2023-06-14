largura = 79
with open("9-6.txt") as ent:
    for linha in ent.readlines():
        if linha[0] == ";":
            continue
        elif linha[0] == ".":
            break
        elif linha[0] == ">":
            print(linha[1:].rjust(largura))
        elif linha[0] == "*":
            print(linha[1:].center(largura))
        elif linha[0] == "=":
            for i in range(40):
                print("=")
            continue
        else:
            print(linha)