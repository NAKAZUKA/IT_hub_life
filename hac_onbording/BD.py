import json
import sqlite3


# конфигурация базы данных (SQLite)
DATABASE = 'BD.db'

# функция для создания подключения к базе данных
def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def get_question(question):
    db = get_db()
    data = db.execute(question).fetchall()
    data = [dict(ix) for ix in data]
    return data