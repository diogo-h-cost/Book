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
        print(f"\nCC N°{self.numero}  Saldo: {self.saldo:.2f}")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}\nTelefone: {cliente.telefone}\n")

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
conta1 = conta([joao], 1238, 500)
conta1.resumo()

jose = cliente("Jose Silva", "987-4123")
conta2 = conta([jose], 797, 500)
conta2.resumo()