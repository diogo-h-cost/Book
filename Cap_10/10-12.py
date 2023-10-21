class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC N°{self.numero} Saldo: {self.saldo:10.2f}\n")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}\nTelefone: {cliente.telefone}\n")

    def pode_saq(self, valor):
        return self.saldo >= valor
    
    def saque(self, valor):
        if self.pode_saq(valor):
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        return False

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC N° {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n    Saldo: {self.saldo:10.2f}\n")

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo = 0, limite = 0):
        super().__init__(clientes, numero, saldo)
        self.limite = limite
    
    def pode_saq(self, valor):
        return self.saldo + self.limite >= valor
    
    def extrato(self):
        Conta.extrato(self)
        print(f"\nLimite: {self.limite}")
        print(f"\nSaldo: {self.saldo + self.limite:.2f}\n")

ki = Cliente("KI KI", "1234")
c1 = ContaEspecial([ki], 1, 100, 100)
c1.extrato()
print(c1.saque(30))
c1.extrato()