# Write your MySQL query statement below
SELECT a1.install_dt, count(a1.player_id) AS installs, 
ROUND(COUNT(a2.event_date)/COUNT(a1.player_id), 2) AS Day1_retention
FROM
(SELECT player_id, min(event_date) install_dt
FROM Activity
GROUP BY player_id) a1
LEFT JOIN Activity a2
on a1.player_id = a2.player_id and date_add(a1.install_dt, interval 1 DAY) = a2.event_date
GROUP BY a1.install_dt
