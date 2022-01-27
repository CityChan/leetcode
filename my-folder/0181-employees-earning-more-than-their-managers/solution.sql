# Write your MySQL query statement below
SELECT e1.name Employee
FROM Employee e1, Employee e2
WHERE e1.managerId=e2.id and e1.salary>e2.salary
