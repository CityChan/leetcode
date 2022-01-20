# Write your MySQL query statement below
# SELECT Request_at as Day,
#        ROUND(COUNT(IF(Status != 'completed', TRUE, NULL)) / COUNT(*), 2) AS 'Cancellation Rate'
# FROM Trips
# WHERE (Request_at BETWEEN '2013-10-01' AND '2013-10-03')
#       AND Client_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
# GROUP BY Request_at;

SELECT request_at day, ROUND(SUM(IF(Status !='completed', 1, 0))/count(*),2) AS "cancellation rate" FROM
(SELECT * FROM Trips WHERE client_id IN (SELECT users_id FROM Users WHERE banned="No" and role = "client")
and driver_id IN (SELECT users_id FROM Users WHERE banned="No" and role = "driver")) T1
Where request_At BETWEEN '2013-10-01' AND '2013-10-03' GROUP BY REQUEST_AT
