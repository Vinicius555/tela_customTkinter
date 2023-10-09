import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("banco_de_dados.db")
curso = conn.cursor()
error = Error


curso.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,email TEXT NOT NULL UNIQUE,password TEXT NOT NULL) ")
