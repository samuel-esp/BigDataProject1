DROP TABLE favorites;

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

CREATE TABLE favorites AS
SELECT UserId, ProductId, Score FROM reviews;
--GROUP BY ProductId, UserId, Score;

SELECT UserId, ProductId, Score
FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY UserId ORDER BY UserId, Score DESC) AS n
    FROM favorites
) AS x
WHERE n <= 5;

--SELECT * FROM favorites ORDER BY UserId, Score DESC LIMIT 50;

DROP TABLE reviews;
DROP TABLE favorites;