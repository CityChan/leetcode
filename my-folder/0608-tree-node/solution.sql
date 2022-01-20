# Write your MySQL query statement below
SELECT id, CASE WHEN ISNULL(p_id) THEN "Root" 
WHEN id not in (SELECT DISTINCT p_id from Tree WHERE NOT ISNULL(p_id)) THEN "Leaf"
ELSE "Inner" END type from Tree order by id
