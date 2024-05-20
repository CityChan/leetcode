# Write your MySQL query statement below
# SELECT id, 
# CASE WHEN mod(id, 2)=1 and id<(SELECT max(id) FROM Seat) THEN LEAD(student, 1) OVER()
# WHEN mod(id, 2)=1 and id=(SELECT max(id) FROM Seat) THEN student
# ELSE LAG(student, 1) OVER() END student
# FROM Seat

# Select case
# when id%2=0 then id-1
# when id%2=1 and id<(select count(*) from seat) then id+1
# else id
# end as id
# , student
# from seat
# order by id asc

# SELECT
# CASE WHEN MOD(id, 2)=0 THEN id-1 
# WHEN MOD(id, 2)=1 AND id!=(SELECT MAX(id) FROM Seat) THEN id+1
# ELSE id END id, student
# FROM Seat
# ORDER BY ID

SELECT id,
CASE WHEN MOD(id, 2)=1 AND id!=max_id THEN LEAD(student, 1) OVER()
WHEN MOD(id, 2)=0 THEN LAG(student, 1) OVER()
ELSE student END student
FROM Seat, (SELECT MAX(id) max_id FROM Seat) MaxID

