import pandas as pd
import psycopg2
from sqlalchemy import create_engine


conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS crew( credit_id text,department text,gender text,id text,job text,name text,profile_path text)")
conn.commit()

#fetching data from csv and transforming it and putting it back to the csv


data = pd.read_csv('Data/credits.csv')
crew = data['crew']
#print(cast[0].get('cast_id'))

df=[] ##crewi=['credit_id','department','gender','id','job','name','profile_path']

for el in crew:
    tem = eval(el)
    for df1 in tem:
        print(df1)
        query = """Insert into crew(credit_id,department,gender,id,job,name,profile_path) values(%s,%s,%s,%s,%s,%s,%s)"""
        val=(df1.get('credit_id', ''),df1.get('department',''),df1.get('gender',''),df1.get('id',''),df1.get('job',''),df1.get('name',''),df1.get('profile_path',''))
        print(val)
        cur.execute(query,val)
    conn.commit()
    #df.append(df1)
#df= pd.DataFrame(df)

#df.to_csv("cast_new.csv")
