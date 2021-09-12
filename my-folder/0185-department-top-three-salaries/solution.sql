# Write your MySQL query statement below
# select d.Name Department, e1.Name Employee, e1.Salary
# from Employee e1 
# join Department d
# on e1.DepartmentId = d.Id
# where 3 > (select count(distinct(e2.Salary)) 
#                   from Employee e2 
#                   where e2.Salary > e1.Salary 
#                   and e1.DepartmentId = e2.DepartmentId
#                   );
                  
SELECT D.Name AS DEPARTMENT, E3.NAME EMPLOYEE, E3.SALARY
FROM (SELECT * FROM EMPLOYEE E1
WHERE 3>(SELECT COUNT(DISTINCT E2.SALARY) FROM EMPLOYEE E2
         WHERE E2.SALARY>E1.SALARY AND E1.DEPARTMENTID = E2.DEPARTMENTID)) E3
LEFT JOIN DEPARTMENT D ON E3.DEPARTMENTID = D.ID
