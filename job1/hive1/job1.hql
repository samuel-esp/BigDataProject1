DROP TABLE reviews;
DROP TABLE convertedYears;
DROP TABLE yearWords;
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

CREATE TABLE yearWords AS
SELECT  exploded_text.word, COUNT(*) as conteggio
FROM
   (SELECT anno, explode(split(Text, ' ')) AS word FROM convertedYears) AS exploded_text
   GROUP BY  anno, exploded_text.word;

--SELECT * FROM yearWords ORDER BY anno

--DROP TABLE reviews
--DROP TABLE yearWords
