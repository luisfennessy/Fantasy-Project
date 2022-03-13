SELECT ClubName, COUNT(PlayerId) AS PlayersLoopholed
FROM player_selection AS emergency
NATURAL JOIN player_round
NATURAL JOIN club
WHERE emergency.ScoreCounted = 1 
AND (emergency.Position = 'DEF emergency' AND NOT 3 IN (SELECT COUNT(*) FROM player_selection AS non_player NATURAL JOIN player_round WHERE non_player.ClubId = emergency.ClubId AND non_player.RoundNumber = emergency.RoundNumber AND non_player.Year = emergency.Year AND non_player.Position = 'DEF')
	OR emergency.Position = 'MID emergency'  AND NOT 4 IN (SELECT COUNT(*) FROM player_selection AS non_player NATURAL JOIN player_round WHERE non_player.ClubId = emergency.ClubId AND non_player.RoundNumber = emergency.RoundNumber AND non_player.Year = emergency.Year AND non_player.Position = 'MID')
	OR emergency.Position = 'RUC emergency'  AND NOT 1 IN (SELECT COUNT(*) FROM player_selection AS non_player NATURAL JOIN player_round WHERE non_player.ClubId = emergency.ClubId AND non_player.RoundNumber = emergency.RoundNumber AND non_player.Year = emergency.Year AND non_player.Position = 'RUC')
	OR emergency.Position = 'FWD emergency'   AND NOT 3 IN (SELECT COUNT(*) FROM player_selection AS non_player NATURAL JOIN player_round WHERE non_player.ClubId = emergency.ClubId AND non_player.RoundNumber = emergency.RoundNumber AND non_player.Year = emergency.Year AND non_player.Position = 'FWD'))
AND (PlayerId, RoundNumber, Year) in (SELECT PlayerId, RoundNumber, Year FROM player_round)
GROUP BY ClubId
ORDER BY PlayersLoopholed DESC;


