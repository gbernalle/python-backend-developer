import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "primeiro_banco.db")
cursor = con.cursor()

def criar_tabela_bd(con,cursor):
  cursor.execute(
    "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (100),email VARCHAR (150))"
  )
  con.commit()

def inserir_registro(con,cursor, nome, email):
  data =  (nome, email)
  #Se trocar valor de data e rodar de novo, irá gerar um novo registro no bd
  cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);', data) 
  con.commit()

def atualizar_registro(con, cursor, nome, email, id):
  data = (nome, email, id)
  cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?',data) #No WHERE geralmente vai chave primária
  con.commit()

atualizar_registro(con,cursor,"Guilherme Novo", "gui@novo.com", 1)