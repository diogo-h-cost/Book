"""
Escreva um programa que leia duas strings e gere uma terceira,
na qual os caracteres da segunda foram retirados da primeira.
1ª string: AATTGGAA
2ª string: TG
3ª string: AAAA
"""

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

terceira = ""

for letra in primeira:
    if letra not in segunda:
        terceira += letra

if terceira == "":
    print("Todos os caracteres foram removidos.")
else:
    print(f"Os caracteres [{segunda}] foram removidos de [{primeira}], gerando: {terceira}")