# Write your MySQL query statement below
SELECT max(salary) AS SecondHighestSalary
From Employee
Where salary < (SELECT max(salary) FROM Employee)
# SELECT DISTINCT e1.salary AS SecondHighestSalary
# FROM Employee e1
# WHERE 1= (SELECT COUNT(DISTINCT e2.salary) FROM Employee e2 WHERE e1.salary<e2.salary)
