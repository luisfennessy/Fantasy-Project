SELECT FirstName, Surname, AVG(Score) - SeasonAverage AS AvgLiftInCloseGames FROM
player NATURAL JOIN
player_round NATURAL JOIN
player_selection NATURAL JOIN
fixture NATURAL JOIN
club NATURAL JOIN
	(SELECT player.PlayerId AS PlayerId, AVG(Score) AS SeasonAverage FROM
    player_season NATURAL JOIN
    player INNER JOIN
    player_round ON player.PlayerId = player_round.PlayerId
    GROUP BY PlayerId) AS player_season
WHERE ABS(HomeScore - AwayScore) < 50
AND (ClubId = HomeClubId OR ClubId = AwayClubId)
AND ScoreCounted = 1
AND PlayerId IN
	(SELECT PlayerId 
    FROM player
    NATURAL JOIN player_selection
    NATURAL JOIN club
    WHERE RoundNumber = 22)
GROUP BY PlayerId
ORDER BY ABS(AvgLiftInCloseGames) DESC;


    

