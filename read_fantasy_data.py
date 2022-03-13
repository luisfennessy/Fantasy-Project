import requests
import json

URL = 'https://fantasy.afl.com.au/afl_draft/api/auth/login'
LOGIN_ROUTE = ''
HEADERS = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.42',
     'origin': 'https://fantasy.afl.com.au', 
     'referer': 'https://fantasy.afl.com.au' + '/',
}
LOGIN_PAYLOAD = {
    'login': 'luis.fennessy@hotmail.com',
    'password': '444444'
}
LEAGUE_ID = '81416' # still need to incorporate this variable

# data access request URLs
# Your completed trades, offers proposed/received
TRADES_URL = 'https://fantasy.afl.com.au/afl_draft/api/teams_draft/trades?league_id=81416&_=1619682052309'
# Recent transactions
TRANSACTIONS_URL = 'https://fantasy.afl.com.au/afl_draft/api/leagues_draft/transaction_history?league_id=81416&round_id=7&team_id=22222&_=1619681637133'
# Your waiver requests
WAIVER_REQ_URL = 'https://fantasy.afl.com.au/afl_draft/api/leagues_draft/waiver_requests?league_id=81416&_=1619660594989'
#
WAIVER_LIST_URL = 'https://fantasy.afl.com.au/afl_draft/api/leagues_draft/waiver_list?league_id=81416&_=1619678427758'
# Waivers that are free?
WAIVER_FREE_URL = 'https://fantasy.afl.com.au/afl_draft/api/leagues_draft/waiver_free?league_id=81416&_=1619678427759'
# AFL Fantasy released 'news'
NEWS_URL = 'https://fantasy.afl.com.au/data/afl/news_fantasy.json?_=1619660594992'
# Retrieves unreadable general facts
CHECK_SUMS_URL = 'https://fantasy.afl.com.au/data/afl/checksums.json?_=1619660594995'
# Coach's box
COACHS_BOX_URL = 'https://fantasy.afl.com.au/afl_draft/api/user/coaches_box?_=1619660595075'
# My favourite players
FAVOURITES_URL = 'https://fantasy.afl.com.au/afl_draft/api/players/favourites?_=1619678083593'
# Order of draft
SHOW_ORDER_URL = 'https://fantasy.afl.com.au/afl_draft/api/leagues_draft/show_order?league_id=81416&details=1&_=1619678083575'
# Access unauthorised
STATS_URL = 'https://fantasy.afl.com.au/data/afl/draft/81416/stats.json?_=1619678981041'
# Access unauthorised - Gambell?
COACH_URL = 'https://fantasy.afl.com.au/data/afl/draft/81416/coach.json?_=1619678981046'
# All 'fantasy coach membership' stats
COACH_MEMBERSHIP_URL = 'https://fantasy.afl.com.au/data/afl/coach/players.json?_=1619679407181'
# AFL round AFL team stats
ROUNDS_URL = 'https://fantasy.afl.com.au/data/afl/rounds.json?_=1619681283178'
# Basic info on AFL teams
SQUADS_URL = 'https://fantasy.afl.com.au/data/afl/squads.json?_=1619682389895'
# Shows the user's draft league overviews
SHOW_MY_DRAFTS_URL = 'https://fantasy.afl.com.au/afl_draft/api/leagues_draft/show_my?_=1621254324021'
# Shows the user's draft league team overviews
SHOW_MY_TEAM_URL = 'https://fantasy.afl.com.au/afl_draft/api/teams_draft/show_my?_=1621254324029'
# Shows the user's classic leagues
SHOW_MY_CLASSIC_URL = 'https://fantasy.afl.com.au/afl_classic/api/leagues_classic/show_my?_=1621254324024'


# More useful URLs. USE .JSON() NOT .TEXT FOR DATA
# Gets a LOT - all indiv prev scores, opponent scores, player id lineups of rnd
LADDER_URL = 'https://fantasy.afl.com.au/afl_draft/api/leagues_draft/ladder?league_id=81416&round=7&_=1619660337010'
# Start and end of the URL to find transactions - in between is rnd number.
RND_TRANSACTIONS_URL_START = 'https://fantasy.afl.com.au/afl_draft/api/leagues_draft/transaction_history?league_id=81416&round_id='
RND_TRANSACTIONS_URL_END = '&team_id=0&_=1619687392703'
# League logistics, draft picks, fixtures
SHOW_URL = 'https://fantasy.afl.com.au/afl_draft/api/leagues_draft/show?id=81416&_=1619660595066'
# Team names, coaches & IDs
TEAMS_URL = 'https://fantasy.afl.com.au/afl_draft/api/leagues_draft/show_teams?league_id=81416&_=1619660595076'
# Players data.
PLAYERS_URL = 'https://fantasy.afl.com.au/data/afl/players.json?_=1619684670086'
# Shows all team's full lineups for all rounds
ROSTERS_URL_START = 'https://fantasy.afl.com.au/afl_draft/api/leagues_draft/rosters?league_id=81416&round='
ROSTERS_URL_END = '&_=1621254325204'

# keys from returned dictionary of scrape_data() function
CLUBS = 'teams'
LEAGUE = 'league'
PLAYERS = 'players'
RESULTS = 'results'
TRANSACTIONS = 'transactions'
ROSTERS = 'rosters'
RELEVANT_DATA_KEY = 'result'

RNDS_THIS_SEASON = 23

def scrape_data():
    # Open a session, login & collect cookies
    s = requests.session()
    login_req = s.post(URL, headers=HEADERS, data=LOGIN_PAYLOAD)
    cookies = login_req.cookies

    # read in json files from relevant URLs
    data = {}
    data[RESULTS] = s.get(LADDER_URL, cookies=cookies).json()[RELEVANT_DATA_KEY]
    data[PLAYERS] = s.get(PLAYERS_URL, cookies=cookies).json()
    data[LEAGUE] = s.get(SHOW_URL, cookies=cookies).json()[RELEVANT_DATA_KEY]
    data[CLUBS] = s.get(TEAMS_URL, cookies=cookies).json()[RELEVANT_DATA_KEY]
    data[TRANSACTIONS] = []
    data[ROSTERS] = []
    for i in range(RNDS_THIS_SEASON):
        data[TRANSACTIONS].append(s.get(RND_TRANSACTIONS_URL_START + str(i+1)
        + RND_TRANSACTIONS_URL_END, cookies=cookies).json()[RELEVANT_DATA_KEY])
        data[ROSTERS].append(s.get(ROSTERS_URL_START + str(i+1)
        + ROSTERS_URL_END, cookies=cookies).json()[RELEVANT_DATA_KEY])

    return data



