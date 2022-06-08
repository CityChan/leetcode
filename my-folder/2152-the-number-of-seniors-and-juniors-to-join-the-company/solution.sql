# Write your MySQL query statement below

WITH C1 AS (SELECT experience, SUM(SALARY) OVER (PARTITION BY experience ORDER BY salary ASC) cumsalary
FROM Candidates)

SELECT "Senior" AS "experience", COUNT(*) AS "accepted_candidates"
FROM C1 where experience = "Senior" and cumsalary <= 70000
UNION ALL
SELECT "Junior" AS "experience", COUNT(*) AS "accepted_candidates"
FROM C1 
where experience = "Junior" 
and cumsalary <= (SELECT 70000-IFNULL(MAX(cumsalary),0) FROM C1 WHERE experience = "Senior" and cumsalary<=70000)

