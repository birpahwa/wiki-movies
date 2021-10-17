import sys

import pandas as pd
import psycopg2
from sqlalchemy import create_engine


conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS keyword( keyword_id int,id text,name text)")
conn.commit()

#fetching data from csv and transforming it and putting it back to the csv


data = pd.read_csv('/Data/keywords.csv')
keyword=data['keywords']
#first_row = data.iloc[0]
#print(first_row)
counter = 0
for el in keyword:
    tem = eval(el)
    for df1 in tem:
        #print(df1)
        query = """Insert into keyword(keyword_id,id,name) values(%s,%s,%s)"""
        val=(int(data.iloc[counter]['id']),df1.get('id','' ),df1.get('name',''))
        #print(data.iloc[counter]['id'])
        cur.execute(query,val)
    conn.commit()
    counter+=1

