class cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC N°{self.numero} Saldo: {self.saldo:10.2f}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"\nExtrato CC N° {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]} {o[1]:.2f}")
        print(f"\n Saldo: {self.saldo:.2f}\n")

joao = cliente("Joao da Silva", "777-1234")
conta1 = conta([joao], 1, 1000)

conta1.extrato()