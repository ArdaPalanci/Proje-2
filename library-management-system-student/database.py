import sqlite3

DB_NAME = "library.db"


def connect_db():
    connection = sqlite3.connect(DB_NAME)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_tables():
    connection = connect_db()
    cursor = connection.cursor()

    with open("schema.sql", "r", encoding="utf-8") as file:
        cursor.executescript(file.read())

    with open("sample_data.sql", "r", encoding="utf-8") as file:
        cursor.executescript(file.read())

    connection.commit()
    connection.close()
