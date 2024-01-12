import sqlite3
from contextlib import closing

with sqlite3.connect("Caminho-completo/precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("UPDATE precos SET preco = preco * 1.10;")