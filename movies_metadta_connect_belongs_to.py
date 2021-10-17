
import pandas as pd
import psycopg2


conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS movies_connects_belongs_to_collection( movie_id text,belong_to_collection_id text)")
conn.commit()

data = pd.read_csv('/Users/birparkash/PycharmProjects/DevOn/Data/movies_metadata.csv', dtype='unicode')
collec = data['belongs_to_collection']
#print((collec))
query = """Insert into movies_connects_belongs_to_collection(movie_id,belong_to_collection_id) values(%s,%s)"""
val = []
counter=0
for ff in collec:
    if isinstance(ff, str):
        el = eval(ff)
        if isinstance(el, dict):
            val.append((int(data.iloc[counter]['id']),el.get('id','')))
            print(val)
    counter+=1
cur.executemany(query, val)
conn.commit()
