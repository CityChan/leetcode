# Write your MySQL query statement below
# SELECT w1.ID 
# FROM Weather w1, Weather w2
# WHERE DATEDIFF(w1.recordDate, w2.recordDate)=1
# and w1.temperature>w2.temperature

# SELECT id FROM
# (SELECT *, LAG(temperature, 1) OVER(ORDER BY recordDate) AS lag_t
# FROM Weather) w
# WHERE temperature>lag_t


SELECT w1.id
FROM Weather w1, Weather w2
WHERE w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
AND w1.temperature>w2.temperature
