DROP TABLE reviews;
DROP TABLE couples;
drop table couples_greater;
drop table similar_couples;
drop table similar_couples_greater;
drop table result;

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

CREATE TABLE couples AS
SELECT l.UserId as LeftUser, l.ProductId, r.UserId as RightUser, l.Score as LeftScore, r.Score as RightScore
FROM reviews l JOIN reviews r
ON l.ProductId = r.ProductId WHERE l.UserId < r.UserId;

CREATE TABLE couples_greater AS
SELECT *
FROM couples WHERE LeftScore >= 4 AND RightScore >= 4;

CREATE TABLE similar_couples AS
SELECT LeftUser, RightUser, COUNT(*) as repetitions
FROM couples_greater
GROUP BY LeftUser, RightUser;

CREATE TABLE similar_couples_greater AS
SELECT LeftUser,RightUser
FROM similar_couples
WHERE repetitions >= 3;

CREATE TABLE result as
SELECT c.LeftUser, ProductId, c.RightUser, LeftScore, RightScore
FROM couples_greater c
where exists (select s.LeftUser, s.RightUser 
              from similar_couples_greater s
              where s.LeftUser = c.LeftUser and s.RightUser = c.RightUser);

select * from result;

DROP TABLE reviews;
DROP TABLE couples;
drop table couples_greater;
drop table similar_couples;
drop table similar_couples_greater;
--drop table result;
