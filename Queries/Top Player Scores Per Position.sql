SELECT * FROM
(SELECT ClubName, FirstName, Surname, Score, Position, RoundNumber
FROM player_selection
NATURAL JOIN player_round
NATURAL JOIN player
NATURAL JOIN club
WHERE ScoreCounted = 1
AND player_selection.Position = 'DEF'
ORDER BY score DESC
LIMIT 5) AS TopDefs
UNION
(SELECT ClubName, FirstName, Surname, Score, Position, RoundNumber
FROM player_selection
NATURAL JOIN player_round
NATURAL JOIN player
NATURAL JOIN club
WHERE ScoreCounted = 1
AND Position = 'MID'
ORDER BY score DESC
LIMIT 5) 
UNION
(SELECT ClubName, FirstName, Surname, Score, Position, RoundNumber
FROM player_selection
NATURAL JOIN player_round
NATURAL JOIN player
NATURAL JOIN club
WHERE ScoreCounted = 1
AND Position = 'RUC'
ORDER BY score DESC
LIMIT 5) 
UNION
(SELECT ClubName, FirstName, Surname, Score, Position, RoundNumber
FROM player_selection
NATURAL JOIN player_round
NATURAL JOIN player
NATURAL JOIN club
WHERE ScoreCounted = 1
AND Position = 'FWD'
ORDER BY score DESC
LIMIT 5);