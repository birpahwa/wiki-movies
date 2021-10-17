import psycopg2


conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS links_small(movieid int,imdbid int,tmdbid int)")
cur.execute("copy links_small FROM '/Users/birparkash/PycharmProjects/DevOn/Data/links_small.csv' DELIMITER ',' CSV")

conn.commit()