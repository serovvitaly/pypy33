import sqlite3

conn = sqlite3.connect('dogs.db')
c = conn.cursor()

result = c.execute("SELECT * FROM owners LIMIT 10")

print(result)