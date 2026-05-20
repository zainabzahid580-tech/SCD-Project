# Refactored from legacy single-file code
import sqlite3

def get_connection():
    return sqlite3.connect('grades.db')

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            math REAL NOT NULL,
            english REAL NOT NULL,
            science REAL NOT NULL,
            total REAL NOT NULL,
            average REAL NOT NULL,
            grade TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
