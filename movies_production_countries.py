import pandas as pd
import psycopg2


conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS movies_production_countries( iso_3166_1 text,name text)")
conn.commit()
data = pd.read_csv('/Users/birparkash/PycharmProjects/DevOn/Data/movies_metadata.csv', dtype='unicode')
collec = data['production_countries']
#print(collec)


for el in collec:
    if isinstance(el, str):
        tem = eval(el)
        if isinstance(tem, list):
            for df1 in tem:
                print(df1)
                query = """Insert into movies_production_countries(iso_3166_1,name) values(%s,%s)"""
                val=(df1.get('iso_3166_1', 0 ),df1.get('name',''))
                print(val)
                cur.execute(query,val)
            conn.commit()