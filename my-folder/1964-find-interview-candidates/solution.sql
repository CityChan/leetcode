# Write your MySQL query statement below
WITH t1 AS
((SELECT contest_id, gold_medal user_id FROM Contests)
UNION
(SELECT contest_id, silver_medal FROM Contests)
UNION
(SELECT contest_id, bronze_medal FROM Contests))

SELECT mail, name FROM Users
WHERE user_id IN 
(SELECT * FROM
(
    SELECT DISTINCT user_id FROM
    (SELECT user_id, contest_id - row_number() over(PARTITION BY user_id ORDER BY contest_id) diff  
    FROM t1) t2
    GROUP BY user_id, diff
    HAVING COUNT(*)>=3
    UNION ALL
    SELECT gold_medal FROM Contests GROUP BY gold_medal HAVING COUNT(*)>=3
) t3)

