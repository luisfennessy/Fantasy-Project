SELECT RoundScore, RoundNumber, Year, ClubName FROM	
    (SELECT HomeScore AS RoundScore, HomeClubId AS ClubId, RoundNumber, Year
	FROM fixture
    WHERE HomeScore < AwayScore
	UNION
	SELECT AwayScore AS RoundScore, AwayClubId, RoundNumber, Year
	FROM fixture
    WHERE AwayScore < HomeScore) AS Scores
NATURAL JOIN club
WHERE RoundScore IS NOT NULL
ORDER BY RoundScore DESC;

