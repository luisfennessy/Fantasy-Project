SELECT FirstName, Surname, AVG(Score) AS AverageInCloseGames, ClubName FROM 
player NATURAL JOIN
player_round NATURAL JOIN
player_selection NATURAL JOIN
fixture NATURAL JOIN
club
WHERE ABS(HomeScore - AwayScore) < 20
AND (ClubId = HomeClubId OR ClubId = AwayClubId)
AND ScoreCounted = 1
GROUP BY PlayerId, ClubName
ORDER BY AverageInCloseGames DESC;

