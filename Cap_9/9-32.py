import os.path

nome = input()

if os.path.exists(nome):
    if os.path.isdir(nome):
        print(f"O diretorio {nome} existe")
    else:
        print(f"{nome} e um arquivo")
else:
    print(f"{nome} nao existe")