# Write your MySQL query statement below
SELECT d.name AS Department, e2.name AS Employee, e2.salary AS Salary
FROM
(SELECT departmentID, MAX(salary) AS max_salary
FROM Employee
GROUP BY departmentId) e1,
Employee e2,
Department d
WHERE e2.departmentId = e1.departmentId AND e2.salary = e1.max_salary AND e2.departmentId = d.id
