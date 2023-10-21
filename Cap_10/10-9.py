class Estado:
    def __init__(self, nome, sigla, cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades

    def exibe_city(self):
        for i in self.cidades:
            print(i.nome, i.populacao)
    
    def sum_populacao(self):
        som = 0
        for i in self.cidades:
            som += i.populacao
        return som

class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

cid1 = Cidade("Garça", 10)
cid2 = Cidade("Marilia", 10)
cid3 = Cidade("Alvaro", 10)

est1 = Estado("São", "SP", [cid1, cid2, cid3])

est1.exibe_city()

print()

print(est1.sum_populacao())