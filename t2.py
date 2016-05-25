import sqlite3
import csv

conn = sqlite3.connect('dogs.db')
c = conn.cursor()

base_url = 'http://ovcharka.kamrbb.ru/?x=prof&id='

with open('users2.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        if row[0] == '#':
            continue
        source_url = base_url + row[0]
        print(source_url)
        c.execute("INSERT INTO owners (source_url, dog_breed, parser_id) VALUES('" + source_url + "', 1, 2)")

conn.commit()
conn.close()