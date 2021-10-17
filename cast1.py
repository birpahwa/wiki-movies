import sys

import pandas as pd
import psycopg2
from sqlalchemy import create_engine


conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS cast1( cast_id text,character text,credit_id text,gender text,id text,name text,order_id text,profile_path text)")
conn.commit()

#fetching data from csv and transforming it and putting it back to the csv


data = pd.read_csv('/Data/credits.csv')
cast = data['cast']


for el in cast:
    tem = eval(el)
    for df1 in tem:
        print(df1)
        query = """Insert into cast1(cast_id,character,credit_id,gender,id,name,order_id,profile_path) values(%s,%s,%s,%s,%s,%s,%s,%s)"""
        val=(df1.get('cast_id', 0 ),df1.get('character',''),df1.get('credit_id',''),df1.get('gender',0),df1.get('id',0),df1.get('name',''),df1.get('order',0),df1.get('profile_path',''))
        print(val)
        cur.execute(query,val)
    conn.commit()

