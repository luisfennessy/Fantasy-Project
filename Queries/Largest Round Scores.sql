SELECT RoundScore, RoundNumber, Year, ClubName FROM	
    (SELECT HomeScore AS RoundScore, HomeClubId AS ClubId, RoundNumber, Year
	FROM fixture
	UNION
	SELECT AwayScore AS RoundScore, AwayClubId AS ClubId, RoundNumber, Year
	FROM fixture) AS Scores
NATURAL JOIN club
WHERE RoundScore IS NOT NULL
ORDER BY RoundScore DESC
LIMIT 10;

