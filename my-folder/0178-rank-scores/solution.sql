# Write your MySQL query statement below
SELECT s3.score, s2.rank from SCORES s3,
(SELECT score, row_number() OVER (ORDER BY score DESC) "rank"
FROM
(SELECT DISTINCT score from SCORES) s1) s2
WHERE s3.score=s2.score
order by s3.score DESC
