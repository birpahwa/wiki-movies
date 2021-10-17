import pandas as pd
import psycopg2


conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS movies_metadata(index text,adult text,budget text,homepage text,id text,imdb_id text,original_language text,original_title text,overview text,popularity text,poster_path text,production_countries text,release_date text,revenue text,runtime  text,spoken_languages text,status text,tagline text,title text,video text,vote_average text,vote_count text)")
conn.commit()
data1=pd.read_csv('/Users/birparkash/PycharmProjects/DevOn/Data/movies_metadata.csv', dtype='unicode')
collect= data1[['adult','budget','homepage','id','imdb_id','original_language','original_title','overview','popularity','poster_path','production_countries','release_date','revenue','runtime','spoken_languages','status','tagline','title','video','vote_average','vote_count']]

collect.to_csv('meta_new.csv')
cur.execute("copy movies_metadata FROM '/Users/birparkash/PycharmProjects/DevOn/wiki&movies/meta_new.csv' DELIMITER ',' CSV")

conn.commit()

