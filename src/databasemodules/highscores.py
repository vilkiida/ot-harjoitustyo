# import sqlite3

# class Highscores:
#     def __init__(self):
#         self.db = sqlite3.connect("highscores.db")
#         self.db.isolation_level = None
#         self.db.execute("CREATE TABLE highscores (id INTEGER PRIMARY KEY, time INTEGER, difficulty TEXT)")

#     def new_score(self, time, difficulty):
#         try:
#             sql="INSERT INTO highscores (time, difficulty) VALUES (?, ?)"
#             self.db.execute(sql, [time, difficulty])
#         except:
#             print("Unable to add to highscores")
#     def get_high_scores(self, difficulty):
#         try:
#             sql = "SELECT time FROM highscores WHERE difficulty = ? ORDER BY time LIMIT 10"
#             highscores = self.db.execute(sql, [difficulty]).fetchall()
#         except:
#             return None
#         return highscores
