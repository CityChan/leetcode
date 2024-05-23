# Write your MySQL query statement below

# WITH C1 AS (SELECT experience, SUM(SALARY) OVER (PARTITION BY experience ORDER BY salary ASC) cumsalary
# FROM Candidates)

# SELECT "Senior" AS "experience", COUNT(*) AS "accepted_candidates"
# FROM C1 where experience = "Senior" and cumsalary <= 70000
# UNION ALL
# SELECT "Junior" AS "experience", COUNT(*) AS "accepted_candidates"
# FROM C1 
# where experience = "Junior" 
# and cumsalary <= (SELECT 70000-IFNULL(MAX(cumsalary),0) FROM C1 WHERE experience = "Senior" and cumsalary<=70000)



WITH c AS
(
    SELECT experience, SUM(salary) OVER (PARTITION BY experience ORDER BY salary ASC) cum_salary
    FROM Candidates
)

SELECT "Senior" AS experience, COUNT(*) AS accepted_candidates
FROM c 
WHERE experience="Senior" AND cum_salary<=70000
UNION
SELECT "Junior" AS experience, COUNT(*) AS accepted_candidates
FROM c
WHERE experience="Junior" 
AND cum_salary<70000-(SELECT IFNULL(max(cum_salary), 0) FROM c WHERE experience="Senior" AND cum_salary<=70000)

