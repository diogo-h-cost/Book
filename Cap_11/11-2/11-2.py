import sqlite3

conexao = sqlite3.connect("Caminho-completo/precos.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM precos")
resul = cursor.fetchall()
for reg in resul:
    print(f"Nome: {reg[0]} | Preco: {reg[1]}")

cursor.close()
conexao.close()