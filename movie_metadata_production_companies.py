import pandas as pd
import psycopg2


conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS movies_connect_production_companies( production_company_id text,movie_id text)")
conn.commit()
data = pd.read_csv('Data/movies_metadata.csv', dtype='unicode')
collec = data['production_companies']
#print(collec)

counter=0
for el in collec:
    if isinstance(el, str):
        tem = eval(el)
        if isinstance(tem, list):
            for df1 in tem:
                if isinstance(df1, dict) and data.iloc[counter]['id'].isnumeric():
                    print(type(df1))
                    print(df1)
                    query = """Insert into movies_connect_production_companies(production_company_id,movie_id) values(%s,%s)"""
                    val=((df1.get('id','' ),int(data.iloc[counter]['id'])))
                    #print(val)
                    cur.execute(query,val)
    counter+=1
conn.commit()