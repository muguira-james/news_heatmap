This uses a partitioned set of hive tables to manage news information.

to use:

first create tables;
hive -f create_zztop.q
hive -f create_today.q

second run processing scripts
hive -f load_data.q
hive -f insert_data.q

table today is partitioned by year, month, day

to create table today

create table today (
       title string,
       link string,
       url string,
       data string
) 

Partitioned by (
	    year=int,
	    month=int
	    day=int
);

table zztop is just a temp table. It holds the json version of the raw data.