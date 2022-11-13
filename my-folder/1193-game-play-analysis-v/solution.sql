# Write your MySQL query statement below
SELECT a1.install_dt, count(*) AS installs,
round(count(a2.event_date)/count(*), 2) AS Day1_retention
FROM
(SELECT player_id, min(event_date) install_dt
FROM Activity
GROUP BY player_id) a1
LEFT JOIN Activity a2
on a1.player_id = a2.player_id and date_add(a1.install_dt, interval 1 DAY) = a2.event_date
GROUP BY a1.install_dt
