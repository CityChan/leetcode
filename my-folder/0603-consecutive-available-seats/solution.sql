# Write your MySQL query statement below
SELECT distinct c1.seat_id
FROM Cinema c1, Cinema c2
WHERE c1.free=1 and c2.free=1
AND (c1.seat_id+1=c2.seat_id or c1.seat_id-1=c2.seat_id)
