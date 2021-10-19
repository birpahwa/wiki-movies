import math

import pandas as pd
import psycopg2


conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS movies_belongs_to_collection( id text,name text,poster_path text,backdrop_path text)")
conn.commit()

data = pd.read_csv('Data/movies_metadata.csv', dtype='unicode')
collec = data['belongs_to_collection']
#print((collec))
query = """Insert into movies_belongs_to_collection(id,name,poster_path,backdrop_path) values(%s,%s,%s,%s)"""
val = []
for ff in collec:
    if isinstance(ff, str):
        el = eval(ff)
        if isinstance(el, dict):
            val.append((el.get('id',''),el.get('name',''),el.get('poster_path',''),el.get('backdrop_path','')))
print(len(val))
print(len(collec))
cur.executemany(query, val)
conn.commit()
