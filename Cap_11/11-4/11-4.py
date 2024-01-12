import sqlite3
from contextlib import closing

val_ini = float(input("Valor inicial: "))

val_fim = float(input("Valor final: "))

print()

with sqlite3.connect("Caminho-completo/precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("SELECT * FROM precos WHERE preco BETWEEN ? AND ?;", (val_ini, val_fim))
        
        for resul in cursor.fetchall():
            print(f"Nome: {resul[0]} | Preco: {resul[1]}")
            if resul is None:
                break