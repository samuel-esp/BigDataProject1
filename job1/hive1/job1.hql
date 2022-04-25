DROP TABLE reviews;
DROP TABLE convertedYears;
drop table explodedTable;
drop table result;

CREATE TABLE IF NOT EXISTS reviews (
Id int,
ProductId string,
UserId string,
ProfileName string,
Score int,
Time int,
Text string)
COMMENT 'Reviews Table'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';

LOAD DATA LOCAL INPATH '/home/simoc/Documents/big_data/archive/Reviews.csv' overwrite INTO TABLE reviews;

--SELECT * from reviews

CREATE TABLE convertedYears AS
SELECT year(from_unixtime((Time))) as anno, Text
FROM reviews;

create table explodedTable as
select anno, word
from convertedYears LATERAL VIEW explode(split(Text, ' ')) singleword AS word;

--select * from explodedTable;

create table result as 
select anno, word, count(word) as ripetizioni_per_anno
from explodedTable
group by anno, word;

--select * from result order by word, ripetizioni_per_anno DESC;