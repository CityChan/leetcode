# Write your MySQL query statement below
SELECT e1.Name Employee from Employee e1 left join Employee e2 on e1.ManagerId=e2.Id where e1.ManagerID IS not NULL and e1.Salary>e2.Salary
