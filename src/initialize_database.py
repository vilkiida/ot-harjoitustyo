from databasemodules.highscore_handling import Highscores

def initialize_database():
    db = Highscores()
    db.drop_table()
    db.create_table()

initialize_database()