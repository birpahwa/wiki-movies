select distinct(cast(id as int)), original_title,EXTRACT(YEAR from TO_DATE(release_date,'YYYY/MM/DD')) as Year, cast(revenue as bigint),cast(budget as bigint), round(cast((cast(budget as float)/ cast(revenue as float)) as numeric),2) as ratio_budget_to_revenue from movies_metadata where cast(revenue as bigint) > 0 order by ratio_budget_to_revenue desc;

create table movie_ratio_budget_to_revenue (id integer, original_title text, year numeric, revenue bigint, budget bigint,ratio_budget_to_revenue numeric);

insert into movie_ratio_budget_to_revenue select distinct(cast(id as int)), original_title,EXTRACT(YEAR from TO_DATE(release_date,'YYYY/MM/DD')) as Year, cast(revenue as bigint),cast(budget as bigint), round(cast((cast(budget as float)/ cast(revenue as float)) as numeric),2) as ratio_budget_to_revenue from movies_metadata where cast(revenue as bigint) > 0 order by ratio_budget_to_revenue desc;

select * from movie_ratio_budget_to_revenue;
