# Write your MySQL query statement below

# SELECT 
# ROUND(COUNT(DISTINCT player_id)/(SELECT count(*) FROM Activity WHERE (player_id, event_date) IN (SELECT player_id, date_add(min(event_date), interval 1 DAY) FROM Activity GROUP BY player_id)), 2)
# FROM Activity

# SELECT player_id, count(event_date) as c
# FROM Activity
# WHERE (player_id, event_date) IN (SELECT player_id, min(event_date) FROM Activity GROUP BY player_id)
# GROUP BY player_id

SELECT
  ROUND(
    COUNT(A1.player_id)
    / (SELECT COUNT(DISTINCT A3.player_id) FROM Activity A3)
  , 2) AS fraction
FROM
  Activity A1
WHERE
  (A1.player_id, A1.event_date) IN (
    SELECT
      A2.player_id,
      DATE_ADD(MIN(A2.event_date), INTERVAL 1 DAY)
    FROM
      Activity A2
    GROUP BY
      A2.player_id
  );
