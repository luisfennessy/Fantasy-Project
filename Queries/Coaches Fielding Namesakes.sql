SELECT ClubName, FirstName, Surname
FROM club NATURAL JOIN player_selection
NATURAL JOIN player
WHERE club.CoachFirstName = player.FirstName;