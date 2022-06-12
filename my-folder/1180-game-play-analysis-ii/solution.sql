# Write your MySQL query statement below
select player_id, device_id
from activity a
where a.event_date = (select min(event_date) from activity where player_id = a.player_id)  
