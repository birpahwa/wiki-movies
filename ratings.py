import psycopg2


conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS ratings(userid int,movieid int,rating float,time_stamp bigint)")

cur.execute("copy ratings FROM 'Data/ratings.csv' DELIMITER ',' CSV")
conn.commit()