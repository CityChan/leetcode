# Write your MySQL query statement below

SELECT id, visit_date, people
FROM
(SELECT *, COUNT(*) OVER (PARTITION BY r) c
FROM
(SELECT id, visit_date, people, (id - row_number() over()) r
FROM Stadium
WHERE people>=100) s1) s2
WHERE c>=3

