primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")
terceira = input("Digite a terceira string: ")

if len(segunda) == len(terceira):
    resultado = ""
    for letra in primeira:
        posição = segunda.find(letra)
        if posição != -1:
            resultado += terceira[posição]
        else:
            resultado += letra

    if resultado == "":
        print("Todos os caracteres foram removidos.")
    else:
        print(f"Os caracteres {segunda} foram substituidos por "
              f"{terceira} em {primeira}, gerando: {resultado}")
else:
    print("ERRO: A segunda e a terceira string devem ter o mesmo tamanho.")