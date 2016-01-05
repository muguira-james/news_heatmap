
insert into table today partition (year='2016', month='1', day='5') select transform (text) 
     using 'python map_keywords.py' as (title, link, source, data) 
     from zzTop;

