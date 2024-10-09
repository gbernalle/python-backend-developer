import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "primeiro_banco.db")
cursor = con.cursor()


def criar_tabela_bd(con, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (100),email VARCHAR (150))"
    )
    con.commit()


def inserir_registro(con, cursor, nome, email):
    data = (nome, email)
    # Se trocar valor de data e rodar de novo, irá gerar um novo registro no bd
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    con.commit()


def atualizar_registro(con, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute(
        "UPDATE clientes SET nome=?, email=? WHERE id=?", data
    )  # No WHERE geralmente vai chave primária
    con.commit()


def excluir_registro(con, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", data)
    con.commit()


def inserir_muitos(con, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    con.commit()


# inserir_registro(con, cursor, "Tester02", "teste@novo.com")
# atualizar_registro(con,cursor,"Guilherme Novo", "gui@novo.com", 1)
# excluir_registro(con, cursor, 3)

dados = [
    ("Tester2", "tester02@gmail.com"),
    ("Tester3", "tester03@gmail.com"),
    ("Tester4", "tester04@gmail.com"),
    ("Tester5", "tester05@gmail.com"),
]

inserir_muitos(con, cursor, dados)
