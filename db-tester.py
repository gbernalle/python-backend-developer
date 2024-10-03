import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "primeiro_banco.db")
cursor = con.cursor()

# cursor.execute(
#   "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (100),email VARCHAR (150))"
# )
# Já está criado então não tem porque ficar disponível

data =  ("Guilherme","gui@gmail.com")

#Se torcar valor de data e rodar de novo, irá gerar um novo registro no bd
cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);', data) 
con.commit()