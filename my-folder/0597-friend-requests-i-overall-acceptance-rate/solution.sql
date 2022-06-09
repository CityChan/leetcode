# Write your MySQL query statement below
SELECT IFNULL(ROUND(COUNT(DISTINCT REQUESTER_ID, ACCEPTER_ID)/ COUNT(DISTINCT sender_id, send_to_id), 2), 0) AS accept_rate
FROM RequestAccepted, FriendRequest

