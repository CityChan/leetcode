# Write your MySQL query statement below
# SELECT activity_date day, COUNT(DISTINCT user_id) active_users
# FROM Activity
# WHERE DATEDIFF('2019-07-27', activity_date)<30 AND DATEDIFF('2019-07-27', activity_date)>=0
# GROUP BY activity_date



SELECT activity_date day, COUNT(DISTINCT user_id) active_users
FROM Activity
WHERE activity_date BETWEEN DATE_SUB("2019-07-27", INTERVAL 29 DAY) AND "2019-07-27"
GROUP BY activity_date
