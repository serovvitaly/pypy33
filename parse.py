import sqlite3
import urllib.request
import re


class parser:
    nic = None
    full_name = None
    email = None
    city = None
    country = None
    birth_date = None
    site = None

    def get_content(self, source_url):
        if source_url is None:
            return None
        with urllib.request.urlopen(source_url) as f:
            page_content = f.read().decode("windows-1251", "ignore")
            return page_content


class borda1(parser):
    def __init__(self, source_url):
        page_content = self.get_content(source_url)
        result = re.findall(
            r"pr\('([^']*)','[^']*','([^']*)','([^']*)','([^']*)','([^']*)','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','([^']*)','([^']*)','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*','([^']*)','[^']*','[^']*','[^']*','[^']*','[^']*','[^']*'\)\;",
            page_content, re.MULTILINE)
        data_mix = result[0]
        # print(data_mix)
        self.nic = data_mix[0]
        self.full_name = data_mix[1]
        self.city = data_mix[2]
        self.country = data_mix[3]
        self.birth_date = data_mix[4]
        self.email = data_mix[5]
        self.site = data_mix[6]
        self.info = data_mix[7]


conn = sqlite3.connect('dogs.db')
c = conn.cursor()

result = c.execute("SELECT ow.id, ow.source_url, ps.name FROM owners ow JOIN parsers ps ON ow.parser_id = ps.id WHERE ow.nic IS NULL")

execute_items = []

for row in result:
    owner_id = row[0]
    source_url = row[1]
    parser_class_name = row[2] + '("' + source_url + '")'
    #print(str(owner_id) + ': ' + source_url)
    parser_obj = eval(parser_class_name)
    data_obj = parser_obj.__dict__
    data_obj['owner_id'] = owner_id
    execute_items.append(data_obj)

c.executemany("UPDATE owners SET nic=:nic, full_name=:full_name, city=:city, country=:country, birth_date=:birth_date, email=:email, site=:site, info=:info WHERE id=:owner_id", execute_items)
conn.commit()
