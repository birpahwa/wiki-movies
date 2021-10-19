create table wikidatafinal(title text,url text, abstract text, subli text)
insert into wikidatafinal select substring(title,12)as title, url,abstract, subli from wikidata


select wikidatafinal.title, wikidatafinal.url, movies_metadata.id,movies_metadata.imdb_id,movies_metadata.overview from wikidatafinal inner join movies_metadata on wikidatafinal.title= movies_metadata.original_title;
