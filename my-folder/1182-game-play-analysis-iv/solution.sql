# Write your MySQL query statement below

SELECT ROUND(count(*)/(SELECT COUNT(distinct player_id) FROM ACTIVITY), 2) as fraction
FROM
(SELECT player_id, count(*) as c
FROM Activity
WHERE (player_id, event_date) IN (SELECT player_id, date_add(min(event_date), interval 1 DAY) FROM Activity GROUP BY player_id)
GROUP BY player_id) c1

# SELECT player_id, count(event_date) as c
# FROM Activity
# WHERE (player_id, event_date) IN (SELECT player_id, min(event_date) FROM Activity GROUP BY player_id)
# GROUP BY player_id
