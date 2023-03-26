#A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4].
# Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.

T = [-10, -8, 0, 1, 2, 5, -2, -4]
max = T[0]
min = T[0]
som = 0
for i in T:

    if i > max:
        max = i
    if i < min:
        min = i
    som += i
print(f"Temperatura máxima: {max} °C \nTemperatura mínima: {min} °C \nTemperatura média: {som / len(T)} °C")