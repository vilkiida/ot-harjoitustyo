import sqlite3

class Highscores:
    def __init__(self):
        self.db = sqlite3.connect("highscores.db")
        self.db.isolation_level = None
        self.db.execute("CREATE TABLE highscores (id INTEGER PRIMARY KEY, time INTEGER, player TEXT, difficulty TEXT)")

    def new_score(self, time, player, difficulty):
        try:
            sql="INSERT INTO highscores (time, player, difficulty) VALUES (?, ?, ?)"
            self.db.execute(sql, [time, player, difficulty])
        except:
            print("Unable to add to highscores")
    def get_high_scores(self, difficulty):
        try:
            sql = "SELECT time, player FROM highscores WHERE difficulty = ? ORDER BY time LIMIT 10"
            highscores = self.db.execute(sql, [difficulty]).fetchall()
        except:
            return None
        return highscores

