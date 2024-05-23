# Write your MySQL query statement below
# WITH q1 AS (SELECT person_name, turn, SUM(weight) OVER (ORDER BY turn) as cumweight FROM Queue)
# SELECT person_name FROM q1
# WHERE cumweight<=1000
# AND turn = (SELECT MAX(turn) FROM q1 WHERE cumweight<=1000)

SELECT person_name FROM
(
    SELECT person_name, SUM(weight) OVER (ORDER BY turn) AS cum_weight
    FROM Queue
    ORDER BY cum_weight DESC
) q
WHERE cum_weight<=1000
LIMIT 1
