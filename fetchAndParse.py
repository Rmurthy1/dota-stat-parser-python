import json
import sqlite3
# for working with json http://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-in-python
# going to use postgres on heroku maybe http://initd.org/psycopg/
    # maybe, its a pain in the ass maybe

# for fetching data see: https://docs.python.org/3.5/howto/urllib2.html
    #from https://docs.python.org/3.5/howto/index.html



# the player class
# currently only has an id for each player
class Player:
    def __init__(self, info):
        self.match_id = info["account_id"]
        self.player_slot = info["player_slot"]
        self.hero_id = info["hero_id"]
    def __repr__(self):
        return str(self.match_id)


class Match:
    def __init__(self, info):
        self.match_id = info["match_id"]
        self.players = info["player_list"]
        self.start_time = info["start_time"]
    def __repr__(self):
        return int(self.match_id)
    def __str__(self):
        return (str(self.match_id) + str(self.start_time))


def main():
    matchList = []

    with open("V001.json") as data_file:
        data = json.load(data_file)



    print (data["result"]["results_remaining"])
    for match in data["result"]["matches"]:
        match_info = {}
        match_info["match_id"] = match["match_id"]
        match_info["start_time"] = match["start_time"]
        player_list = []
        for player in match["players"]:
            player_list.append(Player(player))

        match_info["player_list"] = player_list
        tempString = match["match_id"]
        #print (tempString)
        # make an unnamed match and throw it in the list of matches
        matchList.append(Match(match_info))

    # show me all the matches
    for match in matchList:
        print(str(match))

    con = sqlite3.connect('test.db')

    with con:

        con = sqlite3.connect('test.db')

        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')

        data = cur.fetchone()

        print("SQLite version: %s" % data)
        cur.execute("DROP TABLE IF EXISTS Matches")

        stmt = "PRAGMA table_info(Matches)"
        cur.execute(stmt)
        result = cur.fetchone()
        if result:
            print("there is a table named matches!!!!")
        else:
            print("there is no table named matches! I should probably create it!!")
            #write the headers of the database
            cur.execute("CREATE TABLE Matches(Id INT)")
        #for all the matches in the list, insert them into the table
        for match in matchList:
			# note the trailing comma for a single element tuple
            cur.execute('INSERT INTO Matches VALUES(?)', (match.match_id,))

		# now try to get em back out!
        cur.execute("SELECT * FROM Matches")

        rows = cur.fetchall()

        con.commit()

        for row in rows:
            print (row[0])


if __name__ == "__main__":
    main()
