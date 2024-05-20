# Write your MySQL query statement below
# WITH t1 AS
# (
#     SELECT contest_id, gold_medal user_id FROM Contests
#     UNION
#     SELECT contest_id, silver_medal FROM Contests
#     UNION
#     SELECT contest_id, bronze_medal FROM Contests
# )

# SELECT mail, name FROM Users
# WHERE user_id IN 
# (SELECT * FROM
# (
#     SELECT user_id FROM
#     (SELECT user_id, contest_id - row_number() over(PARTITION BY user_id ORDER BY contest_id) diff  
#     FROM t1) t2
#     GROUP BY user_id, diff
#     HAVING COUNT(*)>=3
#     UNION ALL
#     SELECT gold_medal FROM Contests GROUP BY gold_medal HAVING COUNT(*)>=3
# ) t3)


# WITH t1 AS
# (
#     SELECT contest_id, gold_medal AS user_id FROM Contests
#     UNION
#     SELECT contest_id, silver_medal FROM Contests
#     UNION
#     SELECT contest_id, bronze_medal FROM Contests
# )

# SELECT name, mail
# FROM Users
# WHERE user_id 
# IN
# (
#     SELECT user_id
#     FROM
#     (
#         SELECT user_id, contest_id - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY contest_id) AS diff
#         FROM t1
#     ) t2
#     GROUP BY user_id, diff
#     HAVING COUNT(*)>=3
#     UNION ALL
#     SELECT gold_medal FROM Contests GROUP BY gold_medal HAVING COUNT(*)>=3
# )

WITH AllMedals AS
(
    SELECT contest_id, gold_medal user_id FROM Contests
    UNION
    SELECT contest_id, silver_medal FROM Contests
    UNION
    SELECT contest_id, bronze_medal FROM Contests
)

SELECT name, mail
FROM
(SELECT DISTINCT a1.user_id
FROM AllMedals a1, AllMedals a2
WHERE a1.user_id = a2.user_id
AND a1.contest_id-3<a2.contest_id AND a1.contest_id>a2.contest_id
GROUP BY a1.user_id, a1.contest_id
HAVING COUNT(*)=2
UNION
SELECT gold_medal
FROM Contests
GROUP BY gold_medal
HAVING COUNT(*)>=3) Candidates, Users
WHERE Candidates.user_id = Users.user_id

    
