# Write your MySQL query statement below

WITH c2 AS
(SELECT SUBSTR(p.phone_number, 1, 3) c_code, c1.duration FROM
(SELECT * FROM Calls
UNION ALL
SELECT callee_id as caller_id, caller_id as callee_id, duration FROM Calls) c1
LEFT JOIN Person p
ON c1.caller_id = p.id)

SELECT name as country FROM
(SELECT *
FROM c2
GROUP BY c_code
HAVING AVG(duration)> (SELECT AVG(duration) FROM Calls)) c3
LEFT JOIN Country
on Country.country_code=c3.c_code

