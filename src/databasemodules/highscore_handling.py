import sqlite3
#from sys import exec_prefix
from datetime import datetime

class Highscores:
    def __init__(self):
        self.db = sqlite3.connect("highscores.db")
        self.db.isolation_level = None

    def create_table(self):
        self.db.execute("CREATE TABLE highscores (id INTEGER PRIMARY KEY, date TIMESTAMP, time INTEGER, difficulty TEXT)")

    def new_score(self, date, time, difficulty):
        try:
            sql="INSERT INTO highscores (date, time, difficulty) VALUES (?, ?, ?)"
            self.db.execute(sql, [date, time, difficulty])
        except:
            print("Unable to add to highscores")
    
    def get_high_scores(self, difficulty):
        try:
            sql = "SELECT date, time FROM highscores WHERE difficulty = ? ORDER BY time, date LIMIT 5"
            highscores = self.db.execute(sql, [difficulty]).fetchall()
        except:
            return None
        return highscores
    def drop_table(self):
        try:
            sql = "DROP TABLE highscores"
            self.db.execute(sql)
        except:
            print("Unable to drop table")
    def erase_scores(self, difficulty):
        try:
            sql = "DELETE FROM highscores WHERE difficulty = ?"
            self.db.execute(sql, [difficulty])
        except:
            print(f"Unable to delete all from {self.difficulty} scores")


