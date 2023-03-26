"""
Escreva um programa que leia duas strings. Verifique se a
segunda ocorre dentro da primeira e imprima a posição de início.
1ª string: AABBEFAATT
2ª string: BE
Resultado: BE encontrado na posição 3 de AABBEFAATT
"""

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

posicao = primeira.find(segunda)

if posicao == -1:
    print(f"'{segunda}' não encontrada em '{primeira}'")
else:
    print(f"{segunda} encontrada na posição {posicao} de {primeira}")