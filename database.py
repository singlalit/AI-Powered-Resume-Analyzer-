import sqlite3

# Create or connect to database
conn = sqlite3.connect('resumes.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        skills TEXT,
        filename TEXT
    )
''')

conn.commit()
conn.close()
