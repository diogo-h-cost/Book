import sqlite3
from contextlib import closing

Nome = input("Nome a selecionar: ")
prec_nov = float(input("Insira o preco novo: "))

with sqlite3.connect("Caminho-completo/precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("UPDATE precos SET preco = ? WHERE nome = ?;", (prec_nov, Nome))
        print("Produto atualizado!")