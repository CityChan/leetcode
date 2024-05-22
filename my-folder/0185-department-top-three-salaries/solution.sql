# Write your MySQL query statement below
# SELECT d.name Department, e1.name Employee, e1.salary Salary
# FROM Employee e1, Department d
# WHERE 3>(SELECT count(DISTINCT e2.salary) FROM Employee e2 WHERE e1.salary<e2.salary and e1.departmentID=e2.departmentID)
# and e1.departmentId = d.id


# SELECT d.name AS Department, e.name AS Employee, salary AS Salary
# FROM
# (
#     SELECT *, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS ranking
#     FROM Employee 
# ) e, Department d
# WHERE e.ranking < 4 and e.departmentId = d.id


SELECT d.name AS Department, e1.name AS Employee, salary AS Salary
FROM Employee e1, Department d
WHERE 3>(SELECT COUNT(DISTINCT e2.salary) FROM Employee e2 WHERE e1.salary<e2.salary AND e1.departmentId=e2.departmentId)
AND e1.departmentId = d.id
