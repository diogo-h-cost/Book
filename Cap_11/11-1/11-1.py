import sqlite3

conexao = sqlite3.connect("Caminho/precos.db")
cursor = conexao.cursor()

cursor.execute("CREATE TABLE precos(nome TEXT, preco REAL)")

cursor.execute("INSERT INTO precos(nome, preco) VALUES(?, ?)", ("Arroz", 10.7))

conexao.commit()
cursor.close()
conexao.close()