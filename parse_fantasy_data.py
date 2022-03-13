from read_fantasy_data import *
import mysql.connector


# ______________________________________________________________________________

# SQL connection data to connect and save the data in
HOST = "localhost"
USERNAME = "scraping_user"
PASSWORD = "444444"
DATABASE = "skc_cup"

# Variables to be updated before database update
THIS_YEAR = 2021
RND_JUST_DONE = int(input("What round has just been completed? "))
RNDS_THIS_SEASON = 23
BYE_RND_THIS_SEASON = (12, 13, 14)

# MySQL commands useful for data insertion
CALL = 'call '
INSERT_START = 'INSERT IGNORE INTO '
INSERT_IGNORE_START = 'INSERT IGNORE INTO '
INSERT_MIDDLE = ' VALUES '
END_OF_CMD = ';'
END_VALUES = ',\n'
NULL_VALUE = 'NULL'

CLUBS_PROCEDURE = 'updateclub'
SEASON_PROCEDURE = 'updateseason'
PLAYER_PROCEDURE = 'updateplayer'
PLAYER_ROUND_PROCEDURE = 'updateplayerround'
PLAYER_SEASON_PROCEDURE = 'updateplayerseason'
ROUND_PROCEDURE = 'updateround'
DRAFT_PROCEDURE = 'updatedraft'
PICK_PROCEDURE = 'updatepick'
FIXTURE_PROCEDURE = 'updatefixture'
CAMPAIGN_PROCEDURE = 'updatecampaign'
LADDER_PROCEDURE = 'updateladder'
PLAYER_SELECTION_PROCEDURE = 'updateplayerselection'
TRADE_PROCEDURE = 'updatetrade'
FA_PROCEDURE = 'updatefainteraction'
PLAYER_MOVE_PROCEDURE = 'updateplayermove'


# keys & data values relevant to club table of db
CLUB_TABLE = 'club(ClubId, ClubName, CoachFirstName, CoachSurname)'
CLUB_ID = 'id'
USER_ID = 'user_id'
CLUB_NAME = 'name'
CLUB_FIRST_NAME = 'firstname'
CLUB_SURNAME = 'lastname'
CLUB_PREMIERSHIPS = {'The L-Bombs': 2, 'The 9th Agains': 2, "Jack's  Army": 0,
"Scrowetum": 2, "Angus’ All Stars": 2, "LucaBlues": 1, 'DOOOOMZDAY': 0, 
'Nelsonarians': 0, "Powndaddys Dingleberries": 0, "Forbesy's Fkwits": 0,
"DOOOOMZDAY": 0, 'The Tip-Rats': 0, "Gooshwas greats": 0}
CLUB_ABBREVIATIONS = {'The L-Bombs': 'LBM', "Gooshwas greats": 'GWG', 
'The Tip-Rats': 'TIP', 'LucaBlues': 'LCB', "Angus’ All Stars": 'ALL',
'DOOOOMZDAY': 'DOO', 'Nelsonarians': 'NEL', "Powndaddys Dingleberries": 'DIN',
"Forbesy's Fkwits": 'FKW', "The 9th Agains": '9TH', "Jack's  Army": "ARM",
"Scrowetum": 'SCR'}

# keys & data values relevant to season table of db
SEASON_TABLE = 'season(Year, Code, IsFinals, Subscription, Size, IsPublic, Name\
, FinalsLength, FinalsSize, FinalsStartRound, EndRound, LeagueRank, StartRound, \
SquadFormation, IsKeeper, IsPlayingByes, PointsLast, WaiverPeriod, TradeWaivers,\
 WaiverOrder, RfaPrivacy, ApproveTrade, IsDppAdditions, TogThreshold, \
IsCaptains, EmergencyLimit, Lockout, IsCustomScoring, RegeneratedFrom, \
NumMatchups, PointAverage, TotalPoints, IsCoachesBox, IsEmergencies, RankBy, \
PlateFinalsLength)'
CODE_KEY = 'code'
IS_FINALS_KEY = 'finals'
SUBSCRIPTION_KEY = 'subscription'
NUM_TEAMS_KEY = 'num_teams'
IS_PUBLIC_KEY = 'privacy'
NAME_KEY = 'name'
FINALS_LENGTH_KEY = 'finals_length'
FINALS_SIZE_KEY = 'finals_format'
FINALS_START_KEY = 'finals_start_round'
END_RND_KEY = 'end_round'
START_RND_KEY = 'start_round'
RANK_KEY = 'rank'
SQUAD_FORMATION_KEY = 'squad_size'
IS_KEEPER_KEY = 'keeper'
IS_PLAYING_BYES_KEY = 'bye_rounds'
POINTS_LAST_KEY = 'points_last'
WAIVER_PERIOD_KEY = 'waiver_period'
TRADE_WAIVERS_KEY = 'trade_waivers'
WAIVER_ORDER_KEY = 'waiver_order'
RFA_PRIVACY_KEY = 'rfa_privacy'
APPROVE_TRADE_KEY = 'approve_trade'
IS_DPP_ADDITIONS_KEY = 'original_positions'
TOG_THRESHOLD_KEY = 'tog_threshold'
IS_CAPTAINS_KEY = 'captains'
EMERGENCY_LIMIT_KEY = 'emergency_limit'
LOCKOUT_KEY = 'lockout'
IS_CUSTOM_SCORING_KEY = 'custom_scoring_enabled'
RENEGERATED_KEY = 'regenerated_from'
NUM_MATCHUPS_KEY = 'play_times'
PTS_AVG_KEY = 'points_avg'
TOTAL_PTS_KEY = 'points'
IS_COACHES_BOX = 'coaches_box'
IS_EMERGENCIES_KEY = 'emergency'
RANK_BY_KEY = 'rank_by'
PLATE_FINALS_LENGTH_KEY = 'plate_finals_length'


# keys & data values relevant to player, player rnd & player_season table of db
PLAYER_TABLE = 'player(PlayerId, FirstName, Surname)'
PLAYER_ROUND_TABLE = '`player_round`(PlayerId, Year, RoundNumber, Score, Ranked, \
Tog)'
PLAYER_SEASON_TABLE = '`player_season`(PlayerId, Year, Adp, Ranked, AflTeam, \
OriginalPositionOne, OriginalPositionTwo, AvgTog)'
PLAYER_ID_KEY = 'id'
FIRST_NAME_KEY = 'first_name'
SURNAME_KEY = 'last_name'
AFL_TEAM_KEY = 'squad_id'
PLAYER_SEASON_RANK_KEY = 'season_rank'
PLAYER_STATS_KEY = 'stats'
ADP_KEY = 'adp'
PLAYER_SCORES_KEY = 'scores'
PLAYER_RND_RANK_KEY = 'ranks'
RND_TOG_KEY = 'rd_tog'
SEASON_TOG_KEY = 'tog'
OG_PLAYER_POSITIONS_KEY = 'original_positions'
NEW_PLAYER_POSITIONS_KEY = 'positions'
AFL_TEAM_IDS = {10: 'ADE', 20: 'BRI', 30: 'CAR', 40: 'COL', 50: 'ESS', 60: 
'FRE', 70: 'GEE', 80: 'HAW', 90: 'MEL', 100: 'NTH', 110: 'PTA', 120: 'RIC',
130: 'STK', 140: 'WBD', 1010: 'GWS', 1000: 'GCS', 160: 'SYD', 150: 'WCE'}
POSITION_IDS = {1: 'DEF', 2: 'MID', 3: 'RUC', 4: 'FWD'}

ROUND_TABLE = '`round`(Number, Year, IsPractice)'
FIXTURE_TABLE = 'fixture(HomeClubId, AwayClubId, RoundNumber, Year, HomeScore, \
AwayScore)'
PLAYER_SELECTIONS_TABLE = 'player_selection(Position, ClubId, RoundNumber, \
Year, PlayerId)'
SCORING_PLAYERS_KEY = 'scoring_players'
PLAYERS_KEY = 'players'
LADDER_TABLE = 'ladder(PremiershipPoints, LadderRank, ClubId, RoundNumber, Year)'
PREM_PTS_KEY = 'league_scoreflow'
RANK_HISTORY_KEY = 'rank_history'
FIXTURE_KEY = 'fixture'
WEEKLY_SCORES_KEY = 'scoreflow'
LINEUP_KEY = 'lineup'
BENCH = 'bench'
EMERGENCIES = 'emergency'

CAMPAIGN_TABLE = 'campaign(ClubId, Year, IsCommissioner, IsPlateWinner, \
IsFixtureWinner)'
COMMISSIONER_ID_KEY = 'commissioner'
FIXTURE_WINNER_ID_KEY = 'fixture_winner'
PLATE_WINNER_ID_KEY = 'fixture_plate_winner'

DRAFT_TABLE = 'draft(StartDate, Type, HowOrdered, Year)'
PICK_TABLE = '`pick`(Number, DraftStartDate, ClubId, PlayerId)'
DRAFT_START_KEY = 'draft_start'
DRAFT_TYPE_KEY = 'draft_type'
DRAFT_HOW_ORDERED_KEY = 'draft_order'
DRAFT_PICKS_KEY = 'draft_history'


MISSING_FAS = []
MISSING_TRADES = ['(1, "2021-03-21 14:00:00", 6128, 22214, 2, 2021);',
'(2, "2021-03-29 14:00:00", 30761, 19538, 3, 2021);',
'(3, "2021-03-29 15:00:00", 30761, 7298, 3, 2021);']
TRADE_TABLE = 'trade(TradeId, Date, ClubOneId, ClubTwoId, BeforeRound, \
Year)'
FA_INTERACTION_TABLE = 'fa_interaction(WhenPerformed, Type, RoundNumber, Year, \
ClubId, PlayerId)'
MISSING_PLAYER_MOVES = ['(1, 291962, 6128, 22214);',
'(1, 270938, 22214, 6128);',
'(2, 296359, 30761, 19538);',
'(2, 1002240, 30761, 19538);',
'(2, 296035, 30761, 19538);',
'(2, 294305, 19538, 30761);',
'(3, 290778, 30761, 7298);',
'(3, 293957, 30761, 7298);',
'(3, 992468, 7298, 30761);',
'(3, 291856, 7298, 30761);']
PLAYER_MOVE_TABLE = 'player_move(TradeId, PlayerId, ClubIdFrom, ClubIdTo)'
TRANS_TYPE_KEY = 'type'
FA_PICKUP = 'Add'
FA_DELIST = 'Drop'
TRADE = 'Trade'
TRANS_ID_KEY = 'external_id'
TRANS_DATE_KEY = 'date_iso'
TRANS_CLUB_TO_KEY = 'to_team_id'
TRANS_CLUB_FROM_KEY = 'from_team_id'
TRANS_PLAYER_ID_KEY = 'player_id'


# ______________________________________________________________________________



def invert_int_truth(value):
    '''Converts 0s to 1s, and all other ints to 0s.'''
    if value == 0:
        return 1
    return 0


def get_weekly_scores(club_id, data):
    '''Receives the id of a club and returns the list of the club's weekly 
    scores.'''

    results = data[RESULTS]
    for club in results:
        if club[CLUB_ID] == club_id:
            round_scores = []
            rounds_to_record = [rnd + 1 for rnd in range(RND_JUST_DONE)]
            for rnd in rounds_to_record:
                round_scores.append(club[WEEKLY_SCORES_KEY][str(rnd)])
            return round_scores


def is_playing_byes(season_year):
    '''Accesses database to see whether the league is playing through byes 
    during h&a season.'''

    sql_query = "SELECT IsPlayingByes FROM season WHERE season.Year = " + \
    str(season_year) + ';'
    db = mysql.connector.connect(host=HOST, username=USERNAME, password=PASSWORD, 
        database=DATABASE)
    with db.cursor() as cursor:
        cursor.execute(sql_query)
        return bool(cursor.fetchall()[0][0])


def get_finals_start_rnd(season_year):
    '''Accesses database to see what round the league's finals series starts.'''

    sql_query = "SELECT FinalsStartRound FROM season WHERE season.Year = " + \
    str(season_year) + ';'
    db = mysql.connector.connect(host=HOST, username=USERNAME, password=PASSWORD, 
        database=DATABASE)
    with db.cursor() as cursor:
        cursor.execute(sql_query)
        return cursor.fetchall()[0][0]


def get_club_results(club_id, data):
    '''From the list of results data, returns the element with results pertaining
    to the club of club_id. '''

    results = data[RESULTS]
    for result in results:
        if result[CLUB_ID] == club_id:
            return result
            

# ______________________________________________________________________________


def parse_clubs(data):
    '''Converts the dictionary of clubs data into an excutable SQL statement.'''

    clubs = data[CLUBS]
    queries = []
    for club in clubs:
        queries.append(f'{CALL} {CLUBS_PROCEDURE}("{club[CLUB_ID]}","{club[CLUB_NAME]}",\
            "{club[CLUB_FIRST_NAME]}","{club[CLUB_SURNAME]}", {CLUB_PREMIERSHIPS[club[CLUB_NAME]]},\
            "{CLUB_ABBREVIATIONS[club[CLUB_NAME]]}");')
    return queries


def parse_season(data):
    '''Converts the dictionary of season data into an executable SQL 
    statement.'''

    season = data[LEAGUE]
    queries = []
    queries.append(f"{CALL}{SEASON_PROCEDURE}({THIS_YEAR},'{season[CODE_KEY]}',{season[IS_FINALS_KEY]},'\
    {season[SUBSCRIPTION_KEY]}',{season[NUM_TEAMS_KEY]},{season[IS_PUBLIC_KEY]}\
    ,'{season[NAME_KEY]}',{season[FINALS_LENGTH_KEY]},{season[FINALS_SIZE_KEY]}\
    ,{season[FINALS_START_KEY]},{season[END_RND_KEY]},{season[RANK_KEY]},\
    {season[START_RND_KEY]},'{season[SQUAD_FORMATION_KEY]}',\
    {season[IS_KEEPER_KEY]},{season[IS_PLAYING_BYES_KEY]},\
    {season[POINTS_LAST_KEY]},{season[WAIVER_PERIOD_KEY]},\
    {season[TRADE_WAIVERS_KEY]},{season[WAIVER_ORDER_KEY]},\
    '{season[RFA_PRIVACY_KEY]}','{season[APPROVE_TRADE_KEY]}',\
    {invert_int_truth(season[IS_DPP_ADDITIONS_KEY])},\
    {season[TOG_THRESHOLD_KEY]},{season[IS_CAPTAINS_KEY]},\
    {season[EMERGENCY_LIMIT_KEY]},{season[LOCKOUT_KEY]},\
    {season[IS_CUSTOM_SCORING_KEY]},'{season[RENEGERATED_KEY]}','\
    {season[NUM_MATCHUPS_KEY]}',{season[PTS_AVG_KEY]},{season[TOTAL_PTS_KEY]},\
    {season[IS_COACHES_BOX]},{season[IS_EMERGENCIES_KEY]},\
    '{season[RANK_BY_KEY]}',{season[PLATE_FINALS_LENGTH_KEY]});")
    return queries


def parse_players(data):
    '''Converts the list of player data into an executable SQL 
    statement to populate the 'player' table.'''

    players = data[PLAYERS]
    queries = []
    for player in players:
        queries.append(f'{CALL}{PLAYER_PROCEDURE}({player[PLAYER_ID_KEY]},"{player[FIRST_NAME_KEY]}",\
        "{player[SURNAME_KEY]}");')
    return queries


def parse_rounds(data):
    '''Creates an executable SQL 
    statement to populate the 'round' table.'''

    queries = []
    for i in range(1, RNDS_THIS_SEASON + 1):
        query = f'{CALL}{ROUND_PROCEDURE}({i}, {THIS_YEAR}, '
        if i in BYE_RND_THIS_SEASON and not is_playing_byes(THIS_YEAR):
            query += '1);'
        else:
            query += '0);'
        queries.append(query)
    return queries


def parse_player_rounds(data):
    '''Converts the list of player data into an executable SQL 
    statement to populate the 'player_round' table.'''

    players = data[PLAYERS]
    queries = []
    for player in players:
        player_stats = player[PLAYER_STATS_KEY]
        for rnd in range(1, RND_JUST_DONE + 1):
            if str(rnd) in player_stats[PLAYER_SCORES_KEY].keys():
                if RND_JUST_DONE == rnd and player_stats[RND_TOG_KEY]:
                    tog = player_stats[RND_TOG_KEY]
                elif rnd < RND_JUST_DONE:
                    tog = NULL_VALUE
                queries.append(f'{CALL}{PLAYER_ROUND_PROCEDURE}('\
                f'{player[PLAYER_ID_KEY]}, {THIS_YEAR}, {rnd}, '\
                f'{player_stats[PLAYER_SCORES_KEY][str(rnd)]}, '\
                f'{player_stats[PLAYER_RND_RANK_KEY][str(rnd)]}, {tog},'\
                f' {NULL_VALUE});')
    return queries 


def parse_player_season(data):
    '''Converts the list of player data into an executable SQL 
    statement to populate the 'player_season' table.'''

    players = data[PLAYERS]
    queries = []
    num_players = len(players)
    for i in range(num_players):
        player = players[i]
        player_stats = player[PLAYER_STATS_KEY]
        query = f'{CALL}{PLAYER_SEASON_PROCEDURE}({player[PLAYER_ID_KEY]}, {THIS_YEAR}, {player_stats[ADP_KEY]}\
        , {player_stats[PLAYER_SEASON_RANK_KEY]}, \
        "{AFL_TEAM_IDS[player[AFL_TEAM_KEY]]}", '\
        f'"{POSITION_IDS[player[OG_PLAYER_POSITIONS_KEY][0]]}", '
        if len(player[OG_PLAYER_POSITIONS_KEY]) == 2:
            query += f'"{POSITION_IDS[player[OG_PLAYER_POSITIONS_KEY][1]]}", '
        else:
            query += f'{NULL_VALUE}, '
        query += f'{player_stats[SEASON_TOG_KEY]});'
        queries.append(query)
    return queries
    

def parse_draft(data):
    '''Converts the league data into an executable SQL 
    statement to populate the 'player_season' table.'''

    season = data[LEAGUE]
    return [f'{CALL}{DRAFT_PROCEDURE}("'\
    f'{season[DRAFT_START_KEY].replace("T", " ")[:-6]}", '\
    f'"{season[DRAFT_TYPE_KEY]}", "{season[DRAFT_HOW_ORDERED_KEY]}", '\
    f'{season[DRAFT_START_KEY][0:4]})']


def parse_picks(data):
    '''Converts the league data into an executable SQL 
    statement to populate the 'player_season' table.'''

    queries = []
    season = data[LEAGUE]
    for i in range(len(season[DRAFT_PICKS_KEY])):
        queries.append(f'{CALL}{PICK_PROCEDURE}({i + 1}, \
        "{season[DRAFT_START_KEY].replace("T", " ")[:-6]}", \
        {list(season[DRAFT_PICKS_KEY][i].keys())[0]}, \
        {list(season[DRAFT_PICKS_KEY][i].values())[0]});')
    return queries



def parse_fixtures(data):
    '''Converts the league results data into an executable SQL 
    statement to populate the 'fixture' table.'''

    queries = []
    fixtures = data[LEAGUE][FIXTURE_KEY]
    year_of_fixtures = THIS_YEAR
    for rnd in range(1, RNDS_THIS_SEASON + 1):
        if rnd <= RND_JUST_DONE:
            round_fixture = fixtures[str(rnd)]
            if is_playing_byes(year_of_fixtures) or not(rnd in BYE_RND_THIS_SEASON):
                for matchup in round_fixture:
                    home_team = matchup[0]
                    away_team = matchup[1]
                    queries.append(f'{CALL}{FIXTURE_PROCEDURE}({home_team}, \
                    {away_team}, {rnd}, {THIS_YEAR}, \
                    {get_weekly_scores(home_team, data)[rnd - 1]}, \
                    {get_weekly_scores(away_team, data)[rnd - 1]});')
            else:
                for matchup in round_fixture:
                    home_team = matchup[0]
                    away_team = matchup[1]
                    queries.append(f'{CALL}{FIXTURE_PROCEDURE}({home_team}, {NULL_VALUE}, {rnd}, {THIS_YEAR}, \
                    {get_weekly_scores(home_team, data)[rnd - 1]}, \
                    {NULL_VALUE});')
        elif rnd < get_finals_start_rnd(year_of_fixtures):
            round_fixture = fixtures[str(rnd)]
            for matchup in round_fixture:
                home_team = matchup[0]
                away_team = matchup[1]
                queries.append(f'{CALL}{FIXTURE_PROCEDURE}({home_team}, {away_team}, {rnd}, {THIS_YEAR}, \
                {NULL_VALUE}, {NULL_VALUE});')
    return queries


def parse_campaigns(data):
    '''Converts the league data into an executable SQL 
    statement to populate the 'campaign' table.'''

    queries = []
    season = data[LEAGUE]
    clubs = data[CLUBS]
    year_of_campaign = THIS_YEAR
    commissioner = season[COMMISSIONER_ID_KEY]
    plate_winner = season[PLATE_WINNER_ID_KEY]
    fixture_winner = season[FIXTURE_WINNER_ID_KEY]
    for club in clubs:
        queries.append(f'{CALL}{CAMPAIGN_PROCEDURE}({club[CLUB_ID]}, \
        {THIS_YEAR}, {int(commissioner == club[USER_ID])}\
        , {int(plate_winner == club[CLUB_ID])}, \
        {int(fixture_winner == club[CLUB_ID])});')
    return queries


def parse_ladder(data):
    '''Converts the club data into an executable SQL 
    statement to populate the 'ladder' table.'''

    queries = []
    results = data[RESULTS]
    year_of_ladder = THIS_YEAR
    rounds_to_record = [rnd + 1 for rnd in range(min(RND_JUST_DONE, RNDS_THIS_SEASON - data[LEAGUE][FINALS_LENGTH_KEY]))]
    for club in results:
        current_pts = 0
        for rnd in rounds_to_record:
            current_pts += club[PREM_PTS_KEY][str(rnd)]
            queries.append(f'{CALL}{LADDER_PROCEDURE}({current_pts}, \
            {club[RANK_HISTORY_KEY][str(rnd)]}, \
            {club[CLUB_ID]}, {rnd}, {year_of_ladder});')
    return queries


def parse_player_selections(data):
    '''Converts the results data into an executable SQL 
    statement to populate the 'player selections' table.'''
    
    queries = []
    rosters = data[ROSTERS]
    record_up_to_rnd = RND_JUST_DONE
    rounds_to_record = [rnd + 1 for rnd in range(record_up_to_rnd)]
    rnd_num = 0
    for rnd in rosters[:record_up_to_rnd]:
        rnd_num += 1
        rnd_num = rounds_to_record.pop(0)
        for club in rnd:
            lineup = club[LINEUP_KEY]
            club_results = get_club_results(club[CLUB_ID], data)
            scoring_players = club_results[SCORING_PLAYERS_KEY][str(rnd_num)][PLAYERS_KEY]
            # leave out captain data here?
            # player_selection(Position, ClubId, RoundNumber, Year, PlayerId)
            for line in POSITION_IDS.keys():
                position_lineup = lineup[str(line)]
                for player in position_lineup:
                    score_counted = int(player in scoring_players)
                    queries.append(f'{CALL}{PLAYER_SELECTION_PROCEDURE}("'\
                        f'{POSITION_IDS[line]}", {club[CLUB_ID]}, '\
                        f'{rnd_num}, {THIS_YEAR}, {player}, {score_counted});')
            emergencies = lineup[EMERGENCIES]
            for line in POSITION_IDS.keys():
                emergency_line = emergencies[str(line)]
                if emergency_line != 0:
                    score_counted = int(emergency_line in scoring_players)
                    queries.append(f'{CALL}{PLAYER_SELECTION_PROCEDURE}("{POSITION_IDS[line]} emergency", {club[CLUB_ID]}, '\
                        f'{rnd_num}, {THIS_YEAR}, {emergency_line}, {score_counted});')
            bench = lineup[BENCH]
            for player in bench:
                if player not in emergencies.values():
                    score_counted = int(player in scoring_players)
                    queries.append(f'{CALL}{PLAYER_SELECTION_PROCEDURE}("bench", {club[CLUB_ID]}, '\
                        f'{rnd_num}, {THIS_YEAR}, {player}, {score_counted});')
    return queries


def parse_transactions(data):
    '''Converts the transactions data into an executable SQL statement to 
    populate the 'trades', 'fa_interactions' and 'player_move' tables.'''

    # some transactions are not in web browser api's return:
    trade_queries = [f'{CALL}{TRADE_PROCEDURE}{trade}' for trade in MISSING_TRADES]
    fa_queries = [f'{CALL}{FA_PROCEDURE}{trade}' for trade in MISSING_FAS]
    move_queries = [f'{CALL}{PLAYER_MOVE_PROCEDURE}{trade}' for trade in MISSING_PLAYER_MOVES]

    transactions = data[TRANSACTIONS]
    record_up_to_rnd = min(RNDS_THIS_SEASON, RND_JUST_DONE + 1)
    for rnd in range(1, record_up_to_rnd + 1):
        rnd_transactions = transactions[rnd - 1]
        for transaction in rnd_transactions:
            trans_type = transaction[TRANS_TYPE_KEY]
            if trans_type == FA_PICKUP:
                fa_queries.append(f'{CALL}{FA_PROCEDURE}("{transaction[TRANS_DATE_KEY].replace("T"," ")[:-6]}",\
                 "Add", {rnd}, {THIS_YEAR}, \
                {transaction[TRANS_CLUB_TO_KEY]}, \
                {transaction[TRANS_PLAYER_ID_KEY]});')
            if trans_type == FA_DELIST:
                fa_queries.append(f'{CALL}{FA_PROCEDURE}("{transaction[TRANS_DATE_KEY].replace("T", " ")[:-6]}",\
                 "Drop", {rnd}, {THIS_YEAR}, \
                {transaction[TRANS_CLUB_FROM_KEY]}, \
                {transaction[TRANS_PLAYER_ID_KEY]});')
            if trans_type == TRADE:
                trade_queries.append(f'{CALL}{TRADE_PROCEDURE}({transaction[TRANS_ID_KEY]}, '\
                f'"{transaction[TRANS_DATE_KEY].replace("T", " ")[:-6]}", '\
                f'{transaction[TRANS_CLUB_FROM_KEY]},'\
                f' {transaction[TRANS_CLUB_TO_KEY]}, {rnd}, {THIS_YEAR});')
                move_queries.append(f'{CALL}{PLAYER_MOVE_PROCEDURE}({transaction[TRANS_ID_KEY]}, '\
                f'{transaction[TRANS_PLAYER_ID_KEY]}, '\
                f'{transaction[TRANS_CLUB_FROM_KEY]}, '\
                f'{transaction[TRANS_CLUB_TO_KEY]});')

    return trade_queries, fa_queries, move_queries


def parse_trades(data):
    return parse_transactions(data)[0]

def parse_fa_interactions(data):
    return parse_transactions(data)[1]

def parse_player_moves(data):
    return parse_transactions(data)[2]



# ______________________________________________________________________________
 

