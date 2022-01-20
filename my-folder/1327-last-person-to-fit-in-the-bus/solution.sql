# Write your MySQL query statement below
SELECT a.person_name
FROM Queue as a
WHERE (SELECT SUM(b.weight)
FROM Queue as b
WHERE a.turn >= b.turn) <= 1000
ORDER BY turn DESC
LIMIT 1;
