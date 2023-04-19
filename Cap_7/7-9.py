palavra = input("Digite a palavra secreta: ").lower().strip()

lis = ["X==:==", "X--:", "X--/", "X--0", "X--|", "X", "X-/|/", "X-/", "X-//"]

for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print(lis[0])
    print(lis[1])
    # ----- print("X==:==\nX  :   ")
    print(lis[3] if erros >= 1 else lis[5])
    if erros == 2:
        print(lis[4])
    elif erros == 3:
        print(lis[2])
    elif erros >= 4:
        print(lis[6])
    linha3 = ""
    if erros == 5:
        print(lis[7])
    elif erros >= 6:
        print(lis[8])
    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        break