# Write your MySQL query statement below
SELECT d.name Department, e1.name Employee, e1.salary Salary
FROM Employee e1, Department d
WHERE 3>(SELECT count(DISTINCT e2.salary) FROM Employee e2 WHERE e1.salary<e2.salary and e1.departmentID=e2.departmentID)
and e1.departmentId = d.id
