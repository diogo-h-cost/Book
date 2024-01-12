import sqlite3
from contextlib import closing

nome = input("Nome a selecionar: ")

with sqlite3.connect("Caminho-completo/precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("SELECT * FROM precos WHERE nome = ?", (nome,))
        
        x = 0
        while True:
            resul = cursor.fetchone()
            if resul is None:
                if x == 0:
                    print("Nada encontrado!")
                break
            print(f"Nome: {resul[0]} | Preco: {resul[1]}")
            x += 1