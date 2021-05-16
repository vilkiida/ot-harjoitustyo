""" Moduuli, joka sisältää tietokannan alustavan funktion
"""
from databasemodules.highscore_handling import Highscores
def initialize_database():
    """ Alustaa tietokannan highscoretaulun.
    """
    database = Highscores()
    database.drop_table()
    database.create_table()

initialize_database()
