# Write your MySQL query statement below
SELECT team_name, matches_played, points, goal_for, goal_against, goal_diff
FROM
(
    SELECT home_team_id, COUNT(*) matches_played, 
    SUM(CASE WHEN home_team_goals>away_team_goals THEN 3 
    WHEN home_team_goals=away_team_goals THEN 1 ELSE 0 END) points,
    SUM(home_team_goals) goal_for,  SUM(away_team_goals) goal_against, 
    SUM(home_team_goals)-SUM(away_team_goals) goal_diff
    FROM
    (
        SELECT * FROM Matches
        UNION ALL
        SELECT away_team_id, home_team_id, away_team_goals, home_team_goals FROM Matches
    ) m1
    GROUP BY home_team_id
)t2
LEFT JOIN Teams t1
ON t2.home_team_id = t1.team_id
ORDER BY points DESC, goal_diff DESC, team_name ASC


