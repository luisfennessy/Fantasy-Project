SELECT RoundNumber, Year, ClubName, COUNT(PlayerId) AS TONNING_PLAYERS
FROM player_selection
NATURAL JOIN player_round
NATURAL JOIN club
WHERE player_round.Score >= 100
GROUP BY RoundNumber, Year, ClubId
ORDER BY TONNING_PLAYERS DESC;