import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "primeiro_banco.db")
cursor = con.cursor()

cursor.execute(
  "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (100),email VARCHAR (150))"
)
