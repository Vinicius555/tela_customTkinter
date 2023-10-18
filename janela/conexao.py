import sqlite3

error = sqlite3.Error

conn = sqlite3.connect("banco_de_dados.db")
curso = conn.cursor()

curso.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='usuarios'")
tabela_existe = curso.fetchone()

if not tabela_existe:
    curso.execute("""
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)
    conn.commit()