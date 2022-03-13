from parse_fantasy_data import *
from read_fantasy_data import *
import mysql.connector

def update_data(data):
    db_setup_funcs = [parse_clubs, parse_season, parse_players, parse_rounds, 
    parse_player_season, parse_player_rounds, parse_draft, parse_picks, 
    parse_fixtures, parse_campaigns, parse_ladder, parse_player_selections, 
    parse_trades, parse_fa_interactions, parse_player_moves]
    # Open database connection
    db = mysql.connector.connect(host=HOST, username=USERNAME, password=PASSWORD, 
        database=DATABASE)
    db.get_warnings = True
        
    try:
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        for parse_function in db_setup_funcs:
            
            try:
                # Prepare SQL query to INSERT a record into the database.
                queries = parse_function(data)
                warnings = []
                for query in queries:
                    # Execute the SQL command
                    cursor.execute(query)
                    # Commit your changes in the database
                    db.commit()
                    warning = cursor.fetchwarnings()
                    if warning != [] and warning != None:
                        warnings += warning
                print(f"database updated as per {parse_function} with warnings:",
                 set([warning[1] for warning in warnings]))
            except mysql.connector.Error as error:
                # Rollback in case there is any error
                db.rollback()
                print("{} - database rolled back.".format(error))
    except mysql.connector.Error as error:
        # Rollback in case there is any error
        db.rollback()
        print(f"query was: {query}")
        print("{} - database rolled back.".format(error))
    finally:
        if db.is_connected():
            # disconnect from server
            cursor.close()
            db.close()





        


# ______________________________________________________________________________



# access fantasyscrape module to load in website data
data = scrape_data()
update_data(data)
