# Write your MySQL query statement below
WITH a1 AS
(SELECT activity, COUNT(*) AS num
FROM Friends
GROUP BY activity)

SELECT activity FROM a1
WHERE num<(SELECT max(num) FROM a1)
AND num>(SELECT min(num) FROM a1)
