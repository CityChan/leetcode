# Write your MySQL query statement below
# SELECT l3.id, name FROM
# (SELECT DISTINCT id FROM
# (SELECT id, date_sub(login_date, interval row_number() OVER (PARTITION BY id) DAY) group_date FROM
# (SELECT DISTINCT id, login_date FROM Logins ORDER BY id, login_date) l1) l2
# GROUP BY id, group_date
# HAVING count(*)>=5) l3
# LEFT JOIN Accounts a
# ON l3.id = a.id

SELECT DISTINCT a.id, (SELECT name FROM Accounts WHERE id=a.id) name
FROM Logins a, Logins b
WHERE a.id=b.id
AND DATEDIFF(a.login_date, b.login_date) BETWEEN 1 AND 4
GROUP BY a.id, a.login_date
HAVING COUNT(DISTINCT b.login_date) = 4



