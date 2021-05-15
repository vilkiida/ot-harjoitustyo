import sqlite3
from sys import exec_prefix

class Highscores:
    def __init__(self):
        self.db = sqlite3.connect("highscores.db")
        self.db.isolation_level = None

    def create_table(self):
        self.db.execute("CREATE TABLE highscores (id INTEGER PRIMARY KEY, time INTEGER, difficulty TEXT)")

    def new_score(self, time, difficulty):
        try:
            sql="INSERT INTO highscores (time, difficulty) VALUES (?, ?)"
            self.db.execute(sql, [time, difficulty])
        except:
            print("Unable to add to highscores")
    
    def get_high_scores(self, difficulty):
        try:
            sql = "SELECT time FROM highscores WHERE difficulty = ? ORDER BY time LIMIT 5"
            highscores_temp = self.db.execute(sql, [difficulty]).fetchall()
        except:
            return None
        highscores=[]
        for highscore in highscores_temp:
            highscore=highscore[0]
            highscores.append(highscore)
        return highscores
    def drop_table(self, highscores):
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