# Write your MySQL query statement below
# WITH c1 AS
# (SELECT * FROM Calls
# UNION
# SELECT recipient_id, caller_id, call_time FROM Calls)

# SELECT distinct caller_id as user_id
# FROM c1
# WHERE (c1.caller_id, c1.call_time) in 
# (SELECT caller_id, max(c1.call_time) FROM c1 GROUP BY caller_id, date(call_time))
# OR  (c1.caller_id, c1.call_time) in 
# (SELECT caller_id, min(c1.call_time) FROM c1 GROUP BY caller_id, date(call_time))
# GROUP BY caller_id, date(call_time)
# HAVING COUNT(DISTINCT recipient_id)=1

WITH Full_Calls AS
(
    SELECT * FROM Calls
    UNION
    SELECT recipient_id, caller_id, call_time FROM Calls
),
Ranked_Calls AS
(SELECT *, 
ROW_NUMBER() OVER (PARTITION BY caller_id, DATE(call_time) ORDER BY call_time ASC) AS asc_rank,
ROW_NUMBER() OVER (PARTITION BY caller_id, DATE(call_time) ORDER BY call_time DESC) AS desc_rank
FROM Full_Calls)


SELECT DISTINCT caller_id AS user_id
FROM Ranked_Calls
WHERE asc_rank=1 OR desc_rank=1
GROUP BY caller_id, DATE(call_time)
HAVING COUNT(DISTINCT recipient_id)=1

