# Write your MySQL query statement below
SELECT s.product_id, product_name, report_year, total_amount FROM
(
SELECT 
    product_id, "2018" AS report_year,
    average_daily_sales * (DATEDIFF(LEAST(period_end, "2018-12-31"), period_start)+1) AS total_amount
FROM
    Sales s1
WHERE 
    YEAR(period_start)=2018 or YEAR(s1.period_end)=2018
UNION ALL
SELECT 
    product_id, "2019" AS report_year,
    average_daily_sales * (DATEDIFF(LEAST(period_end, "2019-12-31"), GREATEST(period_start, "2019-01-01"))+1) AS total_amount
FROM
    Sales s1
WHERE 
    YEAR(period_start)<=2019 AND YEAR(s1.period_end)>=2019
UNION ALL
SELECT 
    product_id, "2020" AS report_year,
    average_daily_sales * (DATEDIFF(period_end, GREATEST(period_start, "2020-01-01"))+1) AS total_amount
FROM
    Sales s1
WHERE 
    YEAR(period_start)=2020 or YEAR(s1.period_end)=2020
) s
JOIN
Product p
ON
s.product_id = p.product_id
ORDER BY product_id, report_year
