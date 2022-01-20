# Write your MySQL query statement below
WITH TEMP AS (SELECT employee_id, experience, SUM(salary) OVER (PARTITION BY experience ORDER BY salary) "cumsalary" FROM CANDIDATES),
TEMP1 AS
(SELECT * FROM TEMP WHERE experience="Senior" AND cumsalary<=70000)

SELECT employee_id FROM TEMP1
UNION ALL
SELECT employee_id FROM TEMP WHERE experience="Junior" 
AND cumsalary<(SELECT 70000-IFNULL(MAX(cumsalary),0) FROM TEMP1)
