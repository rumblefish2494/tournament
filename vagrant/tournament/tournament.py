#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    pg = connect()
    c = pg.cursor()
    # set all matches to 0 in players table
    c.execute("update players set matches = 0;")
    pg.commit()
    pg.close()




def deletePlayers():
    """Remove all the player records from the database."""
    pg = connect()
    c = pg.cursor()
    # deletes all rows from players table
    c.execute("delete from players;")
    pg.commit()
    pg.close()

def countPlayers():
    """Returns the number of players currently registered."""

    pg = connect()
    c = pg.cursor()
    # get a count of number of registered players from players table
    c.execute("select count(id) from players;")
    players =  c.fetchall()
    plist = [x[0] for x in players]
    pcount = plist[0]
    pg.close()
    return pcount

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    ADD A SERIAL, PLAYER AND WINS (0) TO PLAYERS TABLE
    Args:
      name: the player's full name (need not be unique).
    """
    pg = connect()
    c = pg.cursor()
    # insert a new player and create a player id into players table. set wins and matches to 0
    query = "insert into players (name, wins) values(%s, %s)", (name,0,)
    c.execute("insert into players (name, wins, matches) values(%s, %s, %s)", (name,0,0,))
    pg.commit()
    pg.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    pg = connect()
    c = pg.cursor()
    # get a table of id, name, wins, and matches ordered by wins from players table
    query = "select id, name, wins, matches from players order by wins;"
    c.execute(query)
    standings = c.fetchall()
    pg.close()
    return standings



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
       winner:  the id number of the player who won
       loser:  the id number of the player who lost
    """
    pg = connect()
    c = pg.cursor()
    # increment matches for both players
    c.execute("update players set matches = matches + 1 where id = (%s) or id = (%s);", (winner, loser))
    # increment wins for the winning player
    c.execute("update players set wins = wins + 1 where id = (%s);", [winner])
    pg.commit()
    pg.close()



def swissPairings():
    """pairs registered players based on wins in a swiss pairing style match
       returns list of tuples of pairs of players for next match
    """
    pg = connect()
    c = pg.cursor()
    i = 0
    player_id = []
    player_name = []
    pairings = []
    c.execute("select id, name from players order by wins desc;")
    standings = c.fetchall()

    for (pid, name) in standings:
        player_id.append(pid) # create ordered list of player ids in order of ranking, highest to lowest
        player_name.append(name) # create ordered list of player names in order of ranking, highest to lowest
    while i < len(player_id):
        pairings.append((player_id[i],player_name[i],player_id[i+1],player_name[i+1])) # pair players by ranking in list of tuples
        i +=2

    pg.close()
    return pairings



