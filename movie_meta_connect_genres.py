import pandas as pd
import psycopg2


conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS movies_connect_genres( genre_id text,movie_id text)")
conn.commit()
data = pd.read_csv('/Users/birparkash/PycharmProjects/DevOn/Data/movies_metadata.csv', dtype='unicode')
collec = data['genres']

query = """Insert into movies_connect_genres(genre_id,movie_id) values(%s,%s)"""
val = []
counter=0
for df in collec:
    if isinstance(df, str):
        df1 = eval(df)
        for el in df1:
            if isinstance(el, dict) and data.iloc[counter]['id'].isnumeric():
                print(el.get('id'))
                print(type(data.iloc[counter]['id']))
                print(counter)
                val.append((el.get('id',''),int(data.iloc[counter]['id'])))
    counter+=1
cur.executemany(query, val)
conn.commit()
