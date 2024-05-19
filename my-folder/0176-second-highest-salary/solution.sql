# Write your MySQL query statement below
# SELECT max(salary) AS SecondHighestSalary
# From Employee
# Where salary < (SELECT max(salary) FROM Employee)
# SELECT DISTINCT e1.salary AS SecondHighestSalary
# FROM Employee e1
# WHERE 1= (SELECT COUNT(DISTINCT e2.salary) FROM Employee e2 WHERE e1.salary<e2.salary)
# SELECT salary SecondHighestSalary FROM
# (SELECT salary, dense_rank() OVER (ORDER BY salary DESC) 'ranking'
# FROM Employee e1) e2
# WHERE e2.ranking=2


# SELECT FIRST_VALUE(salary) OVER(ORDER BY salary) AS SecondHighestSalary
# FROM Employee e1 
# WHERE 1 = (SELECT COUNT(DISTINCT e2.salary) FROM Employee e2 WHERE e2.salary>e1.salary)

# SELECT IFNULL((SELECT DISTINCT SALARY FROM EMPLOYEE ORDER BY SALARY DESC LIMIT 1, 1), NULL)
# FROM Employee e1

# SELECT IFNULL(
#     (SELECT DISTINCT salary SecondHighestSalary
#      FROM Employee e1
#      WHERE (SELECT COUNT(DISTINCT e2.salary) 
#             FROM Employee e2 
#             WHERE e1.salary < e2.salary) = 1), NULL) SecondHighestSalary;

SELECT IFNULL(
(SELECT DISTINCT salary
FROM
(SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) ranking
FROM Employee) e
WHERE e.ranking=2), NULL) SecondHighestSalary 



