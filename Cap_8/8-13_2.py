import random

cont = 0
while cont != 3:
    n = random.randint(1, 10)
    x = int(input("Escolha um numero entre 1 e 10: "))
    if x == n:
        print("Voce acertou!")
        break
    else:
        print("Voce errou.")
        cont += 1