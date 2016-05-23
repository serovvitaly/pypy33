import sqlite3
import urllib.request
import os
import re

conn = sqlite3.connect('dogs.db')
c = conn.cursor()

base_url = 'http://lottas.borda.ru/?13-0-'
base_dir = os.path.dirname(__file__)
cache_dir = os.path.join(base_dir, '.cache')

if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

p = 0

while p <= 5080:
    url = base_url + str(p)
    with urllib.request.urlopen(url) as f:
        page_content = f.read().decode("utf-8", "ignore")
        result = re.findall(r"polz2\('[^']*'\,'[^']*'\,'[^']*'\,'[^']*'\,'[^']*'\,'[^']*'\,'[^']*'\,'[^']*'\,'[^']*'\,'[^']*'\,'([^']*)'\,'[^']*'\,'[^']*'\,'[^']*'\)\;", page_content, re.MULTILINE)
        for nic in result:
            profile_url = 'http://lottas.borda.ru/?32-' + nic
            c.execute("INSERT INTO owners (source_url) VALUES('"+profile_url+"')")
        #cache_file_path = os.path.join(cache_dir, str(p) + '.html')
        #f = open(cache_file_path, 'w')
        #f.write(page_content)
        print(url)
        conn.commit()
    p = p + 40
    

#with urllib.request.urlopen(url) as f:
#    list_arr = dict(f.read())

#c.execute("INSERT INTO owners (vk_id, name) VALUES(324325, 'Ivanko')")


conn.close()
