# Write your MySQL query statement below
SELECT f1.follower, COUNT(DISTINCT f2.follower) num
FROM Follow f1, Follow f2
WHERE f1.follower = f2.followee
GROUP BY f1.follower
ORDER BY f1.follower
