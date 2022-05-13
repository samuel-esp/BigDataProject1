DROP TABLE reviews;
DROP TABLE convertedYears;
drop table explodedTable;
drop table result;
drop table topTenPerYear;

CREATE TABLE IF NOT EXISTS reviews (
Id int,
ProductId string,
UserId string,
ProfileName string,
HelpfullnessNumerator int,
HelpfullnessDenominator int,
Score int,
Time int,
Summary string,
Text string)
COMMENT 'Reviews Table'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';

LOAD DATA LOCAL INPATH '/home/simoc/Documents/big_data/Reviews.csv' overwrite INTO TABLE reviews;

--SELECT * from reviews

CREATE TABLE convertedYears AS
SELECT year(from_unixtime((Time))) as anno, regexp_replace(Text, '\\t', '') as text
FROM reviews;

create table explodedTable as
select anno, word
from convertedYears LATERAL VIEW explode(split(text, ' ')) singleword AS word
where word<>'';

create table result as 
select anno, word, count(word) as ripetizioni_per_anno
from explodedTable
group by anno, word;

create table topTenPerYear as
select anno, word, ripetizioni_per_anno
from (
    select *, ROW_NUMBER() OVER (PARTITION BY anno ORDER BY anno, ripetizioni_per_anno DESC) AS n
    from result
) as x
where n<=10;

select * from topTenPerYear;
