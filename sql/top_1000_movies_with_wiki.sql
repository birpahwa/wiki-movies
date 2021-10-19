-- temp table
create table temp_movies_and_rating (id integer, original_title text, year numeric, revenue bigint, budget bigint,ratio_budget_to_revenue numeric, rating float);
select movie_ratio_budget_to_revenue.id,movie_ratio_budget_to_revenue.original_title, movie_ratio_budget_to_revenue.year,movie_ratio_budget_to_revenue.revenue,movie_ratio_budget_to_revenue.budget,movie_ratio_budget_to_revenue.ratio_budget_to_revenue,Avg(ratings.rating)from movie_ratio_budget_to_revenue inner join ratings on movie_ratio_budget_to_revenue.id=ratings.movieid group by movie_ratio_budget_to_revenue.id,movie_ratio_budget_to_revenue.original_title, movie_ratio_budget_to_revenue.year,movie_ratio_budget_to_revenue.revenue,movie_ratio_budget_to_revenue.budget,movie_ratio_budget_to_revenue.ratio_budget_to_revenue
insert into temp_movies_and_rating select movie_ratio_budget_to_revenue.id,movie_ratio_budget_to_revenue.original_title, movie_ratio_budget_to_revenue.year,movie_ratio_budget_to_revenue.revenue,movie_ratio_budget_to_revenue.budget,movie_ratio_budget_to_revenue.ratio_budget_to_revenue,Avg(ratings.rating)from movie_ratio_budget_to_revenue inner join ratings on movie_ratio_budget_to_revenue.id=ratings.movieid group by movie_ratio_budget_to_revenue.id,movie_ratio_budget_to_revenue.original_title, movie_ratio_budget_to_revenue.year,movie_ratio_budget_to_revenue.revenue,movie_ratio_budget_to_revenue.budget,movie_ratio_budget_to_revenue.ratio_budget_to_revenue
select count(*) from temp_movies_and_rating





--temp table
select wikidatafinal.title, wikidatafinal.url, wikidatafinal.abstract, movies_metadata.id from wikidatafinal inner join movies_metadata on wikidatafinal.title= movies_metadata.original_title;
create table wiki_movies_detail(title text, url text, abstract text, id integer)
insert into wiki_movies_detail select wikidatafinal.title, wikidatafinal.url, wikidatafinal.abstract, movies_metadata.id from wikidatafinal inner join movies_metadata on wikidatafinal.title= movies_metadata.original_title;
select * from wiki_movies_detail;

--temp table
create table temp_wiki_movies_comanies(title text, url text, abstract text, movieid integer,production_company_name text)
select distinct(wiki_movies_detail.title), wiki_movies_detail.url, wiki_movies_detail.abstract, wiki_movies_detail.id,movies_production_companies.name from wiki_movies_detail inner join movies_connect_production_companies on wiki_movies_detail.id =movies_connect_production_companies.movie_id join movies_production_companies on movies_connect_production_companies.movie_id =movies_production_companies.id
insert into temp_wiki_movies_comanies select distinct(wiki_movies_detail.title), wiki_movies_detail.url, wiki_movies_detail.abstract, wiki_movies_detail.id,movies_production_companies.name from wiki_movies_detail inner join movies_connect_production_companies on wiki_movies_detail.id =movies_connect_production_companies.movie_id join movies_production_companies on movies_connect_production_companies.movie_id =movies_production_companies.id
select * from temp_wiki_movies_comanies


--- final table
select temp_movies_and_rating.original_title,temp_movies_and_rating.budget,temp_movies_and_rating.year, temp_movies_and_rating.revenue,round(cast(temp_movies_and_rating.rating as numeric),2) as rating ,temp_movies_and_rating.ratio_budget_to_revenue,temp_wiki_movies_comanies.production_company_name,temp_wiki_movies_comanies.url,temp_wiki_movies_comanies.abstract
from temp_movies_and_rating join temp_wiki_movies_comanies on temp_movies_and_rating.id =temp_wiki_movies_comanies.movieid order by temp_movies_and_rating.ratio_budget_to_revenue desc limit 1000

create table Top1000Movie_AsPerRatio(MovieTitle text,Budget bigint,Year numeric,Revenue bigint,Rating numeric, Ratio_BudgetToRevenue numeric,ProductionCompanyName text,Url text,Abstract text)

insert into Top1000Movie_AsPerRatio select temp_movies_and_rating.original_title,temp_movies_and_rating.budget,temp_movies_and_rating.year, temp_movies_and_rating.revenue,round(cast(temp_movies_and_rating.rating as numeric),2) as rating ,temp_movies_and_rating.ratio_budget_to_revenue,temp_wiki_movies_comanies.production_company_name,temp_wiki_movies_comanies.url,temp_wiki_movies_comanies.abstract
from temp_movies_and_rating join temp_wiki_movies_comanies on temp_movies_and_rating.id =temp_wiki_movies_comanies.movieid order by temp_movies_and_rating.ratio_budget_to_revenue desc limit 1000

--main table-----------------
select * from Top1000Movie_AsPerRatio




