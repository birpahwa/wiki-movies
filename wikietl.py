import pandas as pd
import xml.etree.cElementTree as ET
import psycopg2
import os

from datetime import datetime

conn = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='Password#1'")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS wikidata( title text,url text,abstract text, subli text)")
conn.commit()

# Get the list of all files and directories
path = "/Users/birparkash/Downloads/wikiXml"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(dir_list)

# parsing xml file using Element tree and adding it in a list
for n in dir_list:
    if n.startswith("x"):
        file_path = """/Users/birparkash/Downloads/wikiXml/%s"""%(n)
        print(file_path)
        tree = ET.parse(file_path)

        root = tree.getroot()
        #print(root[0]['doc'].text)
        query = """Insert into wikidata(title,url,abstract,subli) values(%s,%s,%s,%s)"""
        val=[]
        for child in root:
            title = child.find("title").text
            url = child.find("url").text
            abstract = child.find("abstract").text
            sublink = child.find("links")
            subli=[]
            for lss in sublink:
                linktype = lss.attrib.get("linktype")
                anchor = lss.find('anchor').text
                link= lss.find('link').text

                subli.append("""{"linktype": %s, "anchor": %s, "link": %s}"""%(linktype,anchor,link))
            val.append((title,url,abstract,subli))
        cur.executemany(query, val)
        conn.commit()
        print('done')
