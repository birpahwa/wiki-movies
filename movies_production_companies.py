import pandas as pd
import psycopg2


conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS movies_production_companies( name text,id int)")
conn.commit()
data = pd.read_csv('Data/movies_metadata.csv', dtype='unicode')
collec = data['production_companies']
#print(collec)


for el in collec:
    if isinstance(el, str):
        tem = eval(el)
        if isinstance(tem, list):
            for df1 in tem:
                if isinstance(df1, dict):
                    print(type(df1))
                    print(df1)
                    query = """Insert into movies_production_companies(name,id) values(%s,%s)"""
                    val=(df1.get('name','' ),df1.get('id',0))
                    #print(val)
                    cur.execute(query,val)
            conn.commit()