# import sqlite3 
# conn = sqlite3.connect('bo.db')
# cursor = conn.cursor()
# from matplotlib import pyplot as plt
# import nu
# cursor.execute('create table success(id integer, name text, country_code text, district text, population integer)')
# conn.commit()
# cursor.execute("insert into success values(1, 'Emma','EMA', 'Emma', 1000 )")
# cursor.execute("insert into success values(2, 'Oge','OGE', 'Oge', 2000 )")
# cursor.execute("insert into success values(3, 'John','JON', 'John', 3000 )")
# cursor.execute("insert into success values(4, 'Philip','PHP', 'Philip', 4000 )")
# cursor.execute("insert into success values(5, 'Richard','RID', 'Richard', 5000 )")
# cursor.execute("insert into success values(6, 'Ruth','RUT', 'Ruth', 6000 )")
# cursor.execute("insert into success values(7, 'Stanley','STN', 'Stanley', 7000 )")
# cursor.execute("insert into success values(8, 'Onyeka','OKA', 'Onyeka', 8000 )")
# cursor.execute("insert into success values(9, 'Sandra','SDA', 'Sandra', 9000 )")
# cursor.execute("insert into success values(10, 'Okey','OKY', 'Okey', 10000 )")
# conn.commit()
# print('done')

# cursor.execute('select name,population,country_code from success where population between 4000 and 10000')

# users = cursor.fetchall()
# print(users)

import datetime

print(day)