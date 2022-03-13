SELECT ClubName, COUNT(*) AS TenGamePlayers FROM
	(SELECT ClubName, FirstName, Surname, COUNT(*) AS GamesPlayed
	FROM player_selection 
	NATURAL JOIN player 
	NATURAL JOIN club
	WHERE ScoreCounted = 1
	GROUP BY PlayerId, ClubId
	ORDER BY GamesPlayed DESC) AS GamesPlayed
WHERE GamesPlayed >= 10
GROUP BY ClubName
ORDER BY TenGamePlayers DESC;