SELECT ClubName, COUNT(PlayerId) AS PlayersLoopholed
FROM player_selection
NATURAL JOIN player_round
NATURAL JOIN club
WHERE player_selection.ScoreCounted = 1 
AND (player_selection.Position = 'DEF emergency'
	OR player_selection.Position = 'MID emergency' 
	OR player_selection.Position = 'RUC emergency' 
	OR player_selection.Position = 'FWD emergency')
AND (PlayerId, RoundNumber, Year) in (SELECT PlayerId, RoundNumber, Year FROM player_round)
GROUP BY ClubId
ORDER BY PlayersLoopholed DESC;