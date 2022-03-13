SELECT ClubName, FirstName, Surname, AVG(score) AS AvgForTeam, COUNT(*) AS GamesPlayed
FROM player_selection 
NATURAL JOIN player 
NATURAL JOIN club
NATURAL JOIN player_round
WHERE ScoreCounted = 1
GROUP BY PlayerId, ClubId
HAVING GamesPlayed >= 3
ORDER BY AvgForTeam DESC;