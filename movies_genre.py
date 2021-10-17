import pandas as pd
import psycopg2


conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS genres( id text,name text)")
conn.commit()
data = pd.read_csv('/Data/movies_metadata.csv', dtype='unicode')
collec = data['genres']

query = """Insert into genres(id,name) values(%s,%s)"""
val = []
for df in collec:
    if isinstance(df, str):
        df1 = eval(df)
        for el in df1:
            if isinstance(el, dict):
                val.append((el.get('id',''),el.get('name','')))

cur.executemany(query, val)
conn.commit()
