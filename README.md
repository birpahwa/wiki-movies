# WIKI-MOVIES

**Infrastructure**

* Macbook pro with Macintosh HD with 121 GB capacity.
* Processor 1.4 GHz Quad-core intel core i5
* Memory 8 GB 2133 MHz LPDDR3****

**Initial Set up**
* Install Pycharm and python 3.9
* Install postgres server for mac (pgAdmin4)
* install pip3 in pycharm to download supporting libraries
* pip install other supporting libraries such as pandas for reading files, xml.etree.cElementTree for xml files AND psycopg2 for connecting to the postgres server.
* Download zipped data folder from the below drive link. Unzip it and copy data folder in the project.
https://drive.google.com/file/d/1BYHNLOB2F6eVCQy5w66me5t8uIuVRXP5/view?usp=sharing


**Download data files from the links given**
* https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract.xml.gz
* https://www.kaggle.com/rounakbanik/the-movies-dataset/version/7#movies_metadata.csv


**Downloading Data Files**
* Kaggle movies data after unzipping we got multiple csv files of around 998 MB divided into 7 files.
* wikilinks files became approx 7 GB and for local server it was not easy to process the same large file because of the infrastructure, I am  splitting the XML file in to multiple files of around 200 MB each using below command in terminal
"split -b 200m enwiki-latest-abstract.xml".

##### **Ingesting datafiles into postgresql tables**

Written scripts for all tables in different python files which is fetching data from Data folder.
And corresponding tables and data is flown to the respective tables in pgAdmin4 server.


#SQL scripts

SQL scripts are given in the sql folder with 3 files having queries for all 3 points (and temporary tables if needed between to get the final queries) mentioned in the task. you can run it on the pgAdmin server's Query tool.


