import sqlite3

conn = sqlite3.connect('resumes.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM resumes")
rows = cursor.fetchall()

for row in rows:
    print(row)  # This prints all stored resumes in the terminal

conn.close()


