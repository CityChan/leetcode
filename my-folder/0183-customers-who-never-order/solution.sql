# Write your MySQL query statement below
# SELECT c1.name Customers
# FROM Customers c1
# LEFT JOIN Orders o1
# on c1.id=o1.customerId
# Where ISNULL(o1.customerId)

SELECT name Customers
FROM Customers
WHERE id not in (SELECT DISTINCT customerId FROM Orders)
