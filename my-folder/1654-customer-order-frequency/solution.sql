# Write your MySQL query statement below

SELECT c1.customer_id, c1.name

FROM 

(SELECT DISTINCT o1.customer_id AS 'customer_id'
 FROM Product p1 RIGHT JOIN Orders o1
ON o1.product_id=p1.product_id
WHERE MONTH(o1.order_date) IN (6, 7) and YEAR(o1.order_date)=2020
GROUP BY o1.customer_id
HAVING SUM(p1.price*o1.quantity*if(MONTH(o1.order_date)=6, 1, 0))>=100
AND SUM(p1.price*o1.quantity*IF(MONTH(o1.order_date)=7, 1, 0))>=100) t1
LEFT JOIN
CUSTOMERS c1
on t1.customer_id=c1.customer_id
