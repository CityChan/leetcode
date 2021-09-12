# Write your MySQL query statement below
SELECT d.name department, e2.name employee, e2.SALARY
FROM 
EMPLOYEE E2, 
(SELECT MAX(SALARY) as SALARY, departmentid FROM EMPLOYEE GROUP BY DEPARTMENTID) E1,
department d
where E2.SALARY= E1.salary and e2.departmentid=E1.departmentid and e2.departmentid=d.id


