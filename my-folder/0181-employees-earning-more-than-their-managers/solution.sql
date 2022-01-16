/* Write your T-SQL query statement below */
SELECT e1.name Employee
FROM Employee e1, Employee e2
Where e1.managerId = e2.id and e1.salary > e2.salary
