"""
Contando caracteres...
Escreva um programa que gere um dicionário, em que cada chave seja um caractere, 
e seu valor seja o número desse caractere encontrado em uma frase lida.
Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}
"""


frase = input("Digite uma frase para contar as letras: ")
d = {}
for letra in frase:
    if letra != " ": # Para não contar o espaco
        d[letra] = d.get(letra, 0) + 1 # Se a letra existir retorna o valor, se nao retorna 0
print(d)
